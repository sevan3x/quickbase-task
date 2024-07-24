from os import environ
from unittest.mock import patch

from modules.github_client import GithubClient


def github_client_initializes_with_headers():
    gh_client = GithubClient()

    assert gh_client.headers == {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {environ['GITHUB_TOKEN']}",
            "X-GitHub-Api-Version": "2022-11-28"
        }


@patch('requests.get')
def github_client_performs_requests_with_valid_response(mock_requests_get):
    gh_client = GithubClient()

    mock_requests_get.return_value.status_code = 200

    resp = gh_client.get_user_data('test_user')

    mock_requests_get.assert_called_once()
    assert resp.status_code == 200


@patch('requests.get')
def github_client_performs_requests_with_invalid_response(mock_requests_get):
    gh_client = GithubClient()

    mock_requests_get.return_value.status_code = 400

    resp = gh_client.get_user_data('test_user')

    mock_requests_get.assert_called_once()

    # add assertion to cover the logged message when logger is implemented
    assert resp.status_code == 403
