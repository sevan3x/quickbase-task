1. Using the program.

   Using is as simple as running the following command in your command line:
   `python quickbase_task.py -u <github_username> -s <subdomain>`

   This will automatically fetch the data of the Github user and create a contact on the following Freshdesk subdomain with it.

2. Running the tests
   - Open tests/tests_config.py and fix the path to your local one
   - cd QuickbaseTask/tests
   - run `python -m unittest`

Important note: configure your Github and Freshdesk tokens. 
