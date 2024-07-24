from os import environ

import json
import requests


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

        if resp.status_code == 201:
            print("Contact created successfully.")  # implement with Logger
        else:
            print("Failed to create a contact.")  # implement with Logger

        return resp
