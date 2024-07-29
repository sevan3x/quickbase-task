import json

from modules.github_client import GithubClient
from modules.freshdesk_client import FreshdeskClient
from library.logger import logger


def process(github_username, subdomain):
    logger.info(f"Start processing of Github user: '{github_username}' and subdomain '{subdomain}'")

    logger.info("Initializing Github Client...")
    gh_client = GithubClient()

    logger.info("Initializing Freshdesk Client...")
    fd_client = FreshdeskClient()

    logger.info("Getting user data from Github...")
    gh_resp = gh_client.get_user_data(github_username)

    if not gh_resp:
        logger.error(f"Failed processing on Github step. "
                     f"Github username: '{github_username}', subdomain: '{subdomain}'")
        return

    gh_user_data = json.loads(gh_resp.text)

    fd_contact_data = _sort_gh_user_data(gh_user_data)
    logger.debug(f"Prepared contact data: {fd_contact_data}")

    logger.info(f"Sending contact data to Freshdesk...")
    fd_resp = fd_client.send_contact_data(subdomain, fd_contact_data)

    if fd_resp.status_code != 201:
        logger.error(f"Failed processing on Freshdesk step. "
                     f"Github username: '{github_username}', subdomain: '{subdomain}'")
        return

    logger.info(f"Processing of Github username: '{github_username}' and subdomain: '{subdomain}' is done.")


def _sort_gh_user_data(user_data):
    contact_data = {
        'name': user_data['name'],
        'email': user_data['email'],
        'twitter_id': user_data['twitter_username'],
        'unique_external_id': user_data['id'],
        'company_id': user_data['company'],
    }

    return contact_data
