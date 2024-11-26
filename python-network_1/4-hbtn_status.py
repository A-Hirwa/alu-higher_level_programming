#!/usr/bin/python3
"""Fetches status from a specified URL using requests"""

import requests
import sys

if __name__ == "__main__":
    # Default to the first URL
    urls = {
        "intranet": "https://alu-intranet.hbtn.io/status",
        "local": "http://0.0.0.0:5050/status",
    }

    # Use a flag to determine which URL to fetch
    flag = sys.argv[1] if len(sys.argv) > 1 else "intranet"
    url = urls.get(flag, urls["intranet"])

    try:
        # Fetch the URL
        response = requests.get(url, timeout=5)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.exceptions.RequestException as e:
        print("Failed to fetch from {}: {}".format(url, e))
