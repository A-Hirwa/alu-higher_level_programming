#!/usr/bin/python3
"""Fetches status from two URLs using requests"""

import requests

if __name__ == "__main__":
    urls = [
        "https://alu-intranet.hbtn.io/status",
        "http://0.0.0.0:5050/status",
    ]

    for url in urls:
        response = requests.get(url)
        print("Fetching from: {}".format(url))
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
        print()
