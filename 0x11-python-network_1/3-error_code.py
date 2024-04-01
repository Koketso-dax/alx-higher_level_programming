#!/usr/bin/python3
"""
managing error codes.
"""
import urllib.request
import sys
from urllib.error import HTTPError


def fetch_url_body(url):
    """
    Fetches the body of the response for the given URL and decodes it in utf-8.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The decoded body of the response.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
    except HTTPError as e:
        print("Error code: {}".format(e.code))
        return None
    return body

if __name__ == "__main__":
    url = sys.argv[1]
    body = fetch_url_body(url)
    if body is not None:
        print(body)
