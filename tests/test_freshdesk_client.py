from os import environ

import unittest
from unittest.mock import patch

import tests_config
from modules.freshdesk_client import FreshdeskClient


class TestFreshdeskClient(unittest.TestCase):
    def test_freshdesk_client_initializes_with_the_right_token(self):
        fd_client = FreshdeskClient()

        self.assertEqual(fd_client.api_key, environ["FRESHDESK_TOKEN"])

    @patch("modules.github_client.logger.info")
    @patch("modules.github_client.logger.debug")
    @patch('requests.post')
    def test_freshdesk_client_performs_a_valid_post_request(self, mock_requests_post, mock_logger_debug, mock_logger_info):
        fd_client = FreshdeskClient()

        mock_requests_post.return_value.status_code = 201

        resp = fd_client.send_contact_data('test_domain', {'test_key': 'test_value'})

        mock_requests_post.assert_called_once()
        self.assertEqual(resp.status_code, 201)
        mock_logger_debug.assert_called_once_with(f"Freshdesk response: {resp.text}")
        mock_logger_info.assert_called_once_with("Contact created successfully.")

    @patch("modules.github_client.logger.error")
    @patch("modules.github_client.logger.debug")
    @patch('requests.post')
    def test_freshdesk_client_performs_a_invalid_post_request(self, mock_requests_post, mock_logger_debug, mock_logger_error):
        fd_client = FreshdeskClient()

        mock_requests_post.return_value.status_code = 401

        resp = fd_client.send_contact_data('test_domain', {'test_key': 'test_value'})

        mock_requests_post.assert_called_once()
        self.assertEqual(resp.status_code, 401)
        mock_logger_debug.assert_called_once_with(f"Freshdesk response: {resp.text}")
        mock_logger_error.assert_called_once_with("Failed to create a contact.")
