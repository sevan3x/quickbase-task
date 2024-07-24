import json

from github_client import GithubClient
from freshdesk_client import FreshdeskClient


def process(github_username, subdomain):
    gh_client = GithubClient()
    fd_client = FreshdeskClient()

    gh_resp = gh_client.get_user_data(github_username)
    gh_user_data = json.loads(gh_resp.text)

    fd_contact_data = _sort_gh_user_data(gh_user_data)

    fd_client.send_contact_data(subdomain, fd_contact_data)


def _sort_gh_user_data(user_data):
    contact_data = {
        'name': user_data['name'],
        'email': user_data['email'],
        'twitter_id ': user_data['twitter_username'],
        'unique_external_id': user_data['id'],
        'company_id': user_data['company'],
    }

    return contact_data
