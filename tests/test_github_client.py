from os import environ

import unittest
from unittest.mock import patch

import tests_config
from modules.github_client import GithubClient


class TestGithubClient(unittest.TestCase):
    def test_github_client_initializes_with_headers(self):
        gh_client = GithubClient()

        self.assertEqual(gh_client.headers, {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {environ['GITHUB_TOKEN']}",
                "X-GitHub-Api-Version": "2022-11-28"
            })

    @patch("modules.github_client.logger.debug")
    @patch("modules.github_client.logger.info")
    @patch('requests.get')
    def test_github_client_performs_requests_with_valid_response(self, mock_requests_get, mock_logger_info, mock_logger_debug):
        gh_client = GithubClient()

        mock_requests_get.return_value.status_code = 200

        resp = gh_client.get_user_data('test_user')

        mock_logger_info.assert_called_once_with("A request to Github is being made.")
        mock_requests_get.assert_called_once()
        self.assertEqual(resp.status_code, 200)
        mock_logger_debug.assert_called_once_with(f"Github response: {resp.text}")

    @patch("modules.github_client.logger.error")
    @patch('requests.get')
    def test_github_client_performs_requests_with_invalid_response(self, mock_requests_get, mock_logger_error):
        gh_client = GithubClient()

        mock_requests_get.return_value.status_code = 400

        resp = gh_client.get_user_data('test_user')

        mock_requests_get.assert_called_once()

        mock_logger_error.assert_called_once_with("There has been a problem with your requests to Github.")
        self.assertEqual(resp, None)
