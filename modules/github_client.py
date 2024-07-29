from os import environ

import requests

from library.logger import logger


class GithubClient:
    def __init__(self):
        self.main_url = "https://api.github.com/users/"
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {environ['GITHUB_TOKEN']}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def get_user_data(self, username):
        logger.info("A request to Github is being made.")
        resp = requests.get(f"{self.main_url}{username}", headers=self.headers)
        logger.debug(f"Github response: {resp.text}")

        if self._response_status_code_is_erroneous(resp):
            self._warn_erroneous_status_codes(resp)
            return None

        return resp

    @staticmethod
    def _response_status_code_is_erroneous(resp):
        if resp.status_code != 200:
            return True
        return False

    @staticmethod
    def _warn_erroneous_status_codes(resp):
        if resp.status_code == 404:
            logger.error("Github token was not provided.")
        elif resp.status_code == 403:
            logger.error("Provided token permissions are insufficient.")
        elif resp.status_code == 401:
            logger.error("Invalid credentials. Please authenticate.")
        elif resp.status_code == 304:
            logger.error("Not modified since last requested.")
        else:
            logger.error("There has been a problem with your requests to Github.")
