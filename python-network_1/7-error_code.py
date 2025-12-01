#!/usr/bin/python3
"""HTTP helper script: GET, POST, check header, and handle errors."""

import sys
import urllib.request
import urllib.parse
import urllib.error

def fetch_status(url):
    """Fetch URL and print response body."""
    req = urllib.request.Request(url)
    req.add_header("cfclearance", "true")
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

def get_request_id(url):
    """Print the X-Request-Id header from the URL."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.getheader("X-Request-Id"))

def post_email(url, email):
    """POST email and print response body."""
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))

def fetch_with_error_handling(url):
    """GET request and print response or error code."""
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    action = sys.argv[1]  # get_status, get_id, post_email, get_error
    if action == "get_status":
        fetch_status(sys.argv[2])
    elif action == "get_id":
        get_request_id(sys.argv[2])
    elif action == "post_email":
        post_email(sys.argv[2], sys.argv[3])
    elif action == "get_error":
        fetch_with_error_handling(sys.argv[2])
