from os import environ
from unittest.mock import patch

from modules.freshdesk_client import FreshdeskClient


def freshdesk_client_initializes_with_the_right_token():
    fd_client = FreshdeskClient()

    assert fd_client.api_key == environ["FRESHDESK_TOKEN"]


@patch('requests.post')
def freshdesk_client_performs_a_valid_post_request(mock_requests_post):
    fd_client = FreshdeskClient()

    mock_requests_post.return_value.status_code = 201

    resp = fd_client.send_contact_data('test_domain', {'test_key': 'test_value'})

    mock_requests_post.assert_called_once()
    assert resp.status_code == 201


@patch('requests.post')
def freshdesk_client_performs_a_invalid_post_request(mock_requests_post):
    fd_client = FreshdeskClient()

    mock_requests_post.return_value.status_code = 401

    resp = fd_client.send_contact_data('test_domain', {'test_key': 'test_value'})

    mock_requests_post.assert_called_once()
    assert resp.status_code == 401
