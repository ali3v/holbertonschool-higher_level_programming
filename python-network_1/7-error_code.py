#!/usr/bin/python3
"""HTTP helper script using requests: GET, POST, check header, and handle errors."""

import sys
import requests

def fetch_status(url):
    """Fetch URL and print response body."""
    r = requests.get(url, headers={"cfclearance": "true"})
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")

def get_request_id(url):
    """Print the X-Request-Id header from the URL."""
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))

def post_email(url, email):
    """POST email and print response body."""
    r = requests.post(url, data={"email": email})
    print(r.text)

def fetch_with_error_handling(url):
    """GET request and print response or error code."""
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)

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
