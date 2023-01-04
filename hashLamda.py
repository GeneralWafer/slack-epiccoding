import boto3
import json
import logging
import os
import base64
import hmac
import hashlib
import time

from base64 import b64decode
from urllib.parse import parse_qs

def respond(res):
    return {
        'statusCode': '200',
        'body': res,
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    #confirm timesamp doesn't differ from local time (replay attacks)
    timestamp = event["headers"]["X-Slack-Request-Timestamp"]
    if abs(time.time() - float(timestamp)) > 60 * 5:
        response_to_slack = respond("sesame closed")
        return response_to_slack
        exit(0)
    
    #defining variables
    slack_signing_key = "5d5744af544f2fdb42ae487a5df9f68f"
    body = base64.b64decode(event["body"]).decode()
    sig_basestring = 'v0:' + timestamp + ':' + body
    slack_signature = event["headers"]["X-Slack-Signature"]
    slack_signing_key_encoded = slack_signing_key.encode()
    aws_signature = "v0=" + hmac.new( slack_signing_key_encoded, sig_basestring.encode(), hashlib.sha256).hexdigest()
    
    #compare aws & slack digests
    if hmac.compare_digest(aws_signature, slack_signature):
        check = "open sesame"
    else:
        check = "sesame closed"

    print(event["body"])
    response_to_slack = respond(check)
    print("control success")
    return response_to_slack
    
