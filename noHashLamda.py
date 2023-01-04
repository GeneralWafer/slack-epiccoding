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
    check = "open sesame"
    response_to_slack = respond(check)
    return response_to_slack
