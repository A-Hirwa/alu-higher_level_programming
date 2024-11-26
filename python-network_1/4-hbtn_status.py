#!/usr/bin/python3
"""Fetches status from a dynamically selected URL using requests"""

import requests

if __name__ == "__main__":
    # Define the two URLs to try
    urls = [
        "https://alu-intranet.hbtn.io/status",
        "http://0.0.0.0:5050/status",
    ]

    for url in urls:
        try:
            # Attempt to fetch the URL
            response = requests.get(url, timeout=5)
            # If successful, print the response and break the loop
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text))
            break
        except requests.exceptions.RequestException:
            # If the URL fails, try the next one
            continue
