#!/usr/bin/python3
"""
Use github api to display id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = f"https://api.github.com/{username}}"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print("Your GitHub id is:", user_data['id'])
    else:
        print("Failed to fetch user data. Status code:", response.status_code)
