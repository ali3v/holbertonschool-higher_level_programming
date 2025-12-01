k#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib"""

from urllib import request


def fetch_status():
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()

