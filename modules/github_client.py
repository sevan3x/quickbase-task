from os import environ

import requests


class GithubClient:
    def __init__(self):
        self.main_url = "https://api.github.com/users/"
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {environ['GITHUB_TOKEN']}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def get_user_data(self, username):
        resp = requests.get(f"{self.main_url}{username}", headers=self.headers)

        if self._response_status_code_is_erroneous(resp):
            return self._warn_erroneous_status_codes(resp)

        return resp

    @staticmethod
    def _response_status_code_is_erroneous(resp):
        if resp.status_code != 200:
            return True
        return False

    @staticmethod
    def _warn_erroneous_status_codes(resp):
        """
        This function is supposed to be implemented with logger
        instead of just returning/printing these statements.
        """
        if resp.status_code == 404:
            return "Github token was not provided."
        elif resp. status_code == 403:
            return "Provided token permissions are insufficient."
        elif resp.status_code == 401:
            return "Invalid credentials. Please authenticate."
        elif resp.status_code == 304:
            return "Not modified since last requested."
        else:
            return "There has been a problem with your requests to Github."
