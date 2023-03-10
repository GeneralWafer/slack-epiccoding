import requests

def sendPayload(url, signature):
    payload = "dG9rZW49OWdPcXpwQlRwYU9TRkhPdDh3cFNYbUlXJnRlYW1faWQ9VDA0RUY2R0pRSjImdGVhbV9kb21haW49ZXBpY2NvZGluZ2NvbSZjaGFubmVsX2lkPUQwNEVSTVZKTDVBJmNoYW5uZWxfbmFtZT1kaXJlY3RtZXNzYWdlJnVzZXJfaWQ9VTA0RU1RMlJWUUEmdXNlcl9uYW1lPW1pb2NldmljaG1pY2hhZWwmY29tbWFuZD0lMkZ0ZXN0JnRleHQ9aGVsbG8rYWtmbm9rYXdmJTVDJmFwaV9hcHBfaWQ9QTA0RVA0VVQyVVQmaXNfZW50ZXJwcmlzZV9pbnN0YWxsPWZhbHNlJnJlc3BvbnNlX3VybD1odHRwcyUzQSUyRiUyRmhvb2tzLnNsYWNrLmNvbSUyRmNvbW1hbmRzJTJGVDA0RUY2R0pRSjIlMkY0NDk5MjAwNTE0ODM1JTJGeVVMNjdxbmM2Um1OVUVsNFNkZlB0ZldIJnRyaWdnZXJfaWQ9NDQ5MjcxMzM5ODkzNC40NDkxMjIwNjM2NjE0LjJmMTkwZThlOWIxNWEwYzhmNTAxYTJlNjdjZDVmYjI0"
    headers = {
      'X-Slack-Request-Timestamp': '1670750774',
      'X-Slack-Signature': signature,
      'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

urlNoHashLamda = "https://9m4lww10jk.execute-api.ap-southeast-2.amazonaws.com/default/noHashLamda"
urlNoRepeatCheck = "https://njyxhm3oz9.execute-api.ap-southeast-2.amazonaws.com/default/hashNoReplayCheck"
urlHashLamda = "https://jxtuwzb397.execute-api.ap-southeast-2.amazonaws.com/default/hashLamda"

oldSignature = 'v0=8b71ad7a919dddb0887440bcf7a0e7fabc7624d56eb678c0ae88881866499a33'
bogusSignature = 'v0=9b71ad7a919dddb0887430bcf7a0e7fabc7624d56eb678c0ae88881866499a34'
noSignature = ''

accessGranted = 'open sesame'
accessDenied = 'sesame closed'

#testing noHashLamda with no signature
def test_noHashLamdaNoSignature():
    assert sendPayload(urlNoHashLamda, noSignature) == accessDenied

#testing noHashLamda with bogus signature
def test_noHashLamdaBogusSignature():
    assert sendPayload(urlNoHashLamda, bogusSignature) == accessDenied

#testing noHashLamda with old signature
def test_noHashLamdaOldSignature():
    assert sendPayload(urlNoHashLamda, oldSignature) == accessDenied

#testing with noRepeat checks, with no signature 
def test_noRepeatCheckNoSignature():
    assert sendPayload(urlNoRepeatCheck, noSignature) == accessDenied

#testing with noRepeat checks, with bogus signature 
def test_noRepeatCheckBogusSignature():
    assert sendPayload(urlNoRepeatCheck, bogusSignature) == accessDenied

#testing with noRepeat checks, with old signature 
def test_noRepeatCheckOldSignature():
    assert sendPayload(urlNoRepeatCheck, oldSignature) == accessDenied

#testing with hashLamda checks, with no signature 
def test_hashLamdaNoSignature():
    assert sendPayload(urlHashLamda, noSignature) == accessDenied

#testing with hashLamda checks, with bogus signature 
def test_hashLamdaBogusSignature():
    assert sendPayload(urlHashLamda, bogusSignature) == accessDenied

#testing with hashLamda checks, with old signature 
def test_hashLamdaOldSignature():
    assert sendPayload(urlHashLamda, oldSignature) == accessDenied