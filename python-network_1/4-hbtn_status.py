#!/usr/bin/python3
"""Fetches status from a single URL using requests"""

import requests

if __name__ == "__main__":
    # Define the two possible URLs
    urls = [
        "https://alu-intranet.hbtn.io/status",
        "http://0.0.0.0:5050/status",
    ]

    for url in urls:
        try:
            # Try fetching the URL
            response = requests.get(url, timeout=5)
            print("Fetching from: {}".format(url))
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text))
            break  # Exit loop once a successful response is fetched
        except requests.exceptions.RequestException as e:
            # Print error and continue trying the next URL
            print("Failed to fetch from {}: {}".format(url, e))
