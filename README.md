# slack-epiccoding
Slack demonstration of importance of signing keys

Uses different lamda functions with different hash checking algorithms to demonstrate why signing keys are needed to combat replay attacks.

PROJECT NOTES (for later reference)
______________

Uses AWS lamda functions to contain hash checking functions.
Slack is used as the endpoint app which is what we are trying to access.
API gateway on AWS is the access-point where which we use in vulntesting.py to access slack server.

Timestamp is required to check that signature is no older than 5 minutes, preventing a hacker who has obtained logs through network sniffing
or other means from using the acquired signature to execute commands through the API gateway.

The 3 different lamda functions demonstrate how AWS will block access if there is hash checking implemented into the gateway.

import requests in vulntesting.py uses request functions to send payloads to websites. In this project it used to send requests to slack via the API gateway.

The signature is only valid if it has a corresponding timestamp which matches the signature.

Cloudwatch logs can be used to debug lamda logs.

POSTMAN is helpful to code the request code the request algorithm used in vulntesting.py.

1. Open in VSCode in dev container
2. Run ```pip install -r "requirements.txt"```
3. Run ```pytest -v```

This should output 4 tests failed and 5 tests passed.

The tests are to check if the lamda functions are behaving as required
given the test.txt scenarios.

There are 3 tests per function. All tests must pass for the function to be
considered "secure" in terms of signing key secrecy.

references:
https://api.slack.com/authentication/verifying-requests-from-slack
