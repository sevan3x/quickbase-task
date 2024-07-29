import unittest
from unittest.mock import patch

import tests_config
from modules.processor import process


class TestProcessor(unittest.TestCase):
    @patch('requests.post')
    @patch('requests.get')
    @patch("modules.github_client.logger.debug")
    @patch("modules.github_client.logger.info")
    def test_processor_completes_successfully(self, mock_logger_info, mock_logger_debug,
                                              mock_requests_get, mock_requests_post):

        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.text = ('{"name": "test_username",'
                                               '"email": "test@mail.com",'
                                               '"twitter_username": "test_twitter_id",'
                                               '"id": "test_id",'
                                               '"company": "test_company_id"}')
        mock_requests_post.return_value.status_code = 201

        process("test_username", "test_subdomain")

        mock_logger_info.assert_any_call("Start processing of Github user: 'test_username' and subdomain 'test_subdomain'")
        mock_logger_info.assert_any_call("Initializing Github Client...")
        mock_logger_info.assert_any_call("Initializing Freshdesk Client...")

        mock_logger_info.assert_any_call("Getting user data from Github...")
        mock_requests_get.assert_called_once()

        contact_data = {"name": "test_username",
                        "email": "test@mail.com",
                        "twitter_id": "test_twitter_id",
                        "unique_external_id": "test_id",
                        "company_id": "test_company_id"}
        mock_logger_debug.assert_any_call(f'Prepared contact data: {contact_data}')

        mock_logger_info.assert_any_call(f"Sending contact data to Freshdesk...")
        mock_requests_post.assert_called_once()

        mock_logger_info.assert_called_with("Processing of Github username: 'test_username' and subdomain: 'test_subdomain' is done.")
