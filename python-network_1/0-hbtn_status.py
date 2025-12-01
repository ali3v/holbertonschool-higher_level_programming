#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status using urllib.
urllib.request is used for fetching URLs [2].
"""
import urllib.request
import urllib.error



def fetch_status():
    """
    Fetches the status URL and prints the body response details.
    """
    url = 'https://intranet.hbtn.io/status'



    headers = {
        'cfclearance': 'true'
    }


    req = urllib.request.Request(url, headers=headers)

    print("Body response:")

    try:

        with urllib.request.urlopen(req) as response:
            content = response.read()

            utf8_content = content.decode('utf-8')

            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(utf8_content))

    except urllib.error.URLError as e:

        if hasattr(e, 'reason'):

            print("\t- Serverə çatmaq mümkün olmadı: {}".format(e.reason))
        elif hasattr(e, 'code'):

            print("\t- Sorğu yerinə yetirilə bilmədi. Kod: {}".format(e.code))


if __name__ == "__main__":
    fetch_status()
