#!/usr/bin/python3
"""Fetched from https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    try:
        request = urllib.request.Request("https://intranet.hbtn.io/status")
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except:
        request = urllib.request.Request("http://0.0.0.0:5050/status")
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
