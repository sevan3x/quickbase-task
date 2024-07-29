from os import environ

import json
import requests

from library.logger import logger


class FreshdeskClient:
    def __init__(self):
        self.api_key = environ["FRESHDESK_TOKEN"]
        self.password = "x"
        self.headers = {
            "Content-Type": "application/json"
        }

    def send_contact_data(self, subdomain, contact):
        resp = requests.post(f"https://{subdomain}.freshdesk.com/api/v2/contacts",
                             auth=(self.api_key, self.password),
                             data=json.dumps(contact),
                             headers=self.headers)

        logger.debug(f"Freshdesk response: {resp.text}")

        if resp.status_code == 201:
            logger.info("Contact created successfully.")
            return resp
        else:
            logger.error("Failed to create a contact.")
            return resp
