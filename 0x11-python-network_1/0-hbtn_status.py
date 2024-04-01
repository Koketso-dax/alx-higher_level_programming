#!/usr/bin/python3
"""
Python script to fetch url using urllib.
"""
import urllib.request


def fetch_status(url):
    """
    Fetches the status from the specified URL using urllib.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        bytes: The content of the response body.
    """
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    html = fetch_status(url)

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
