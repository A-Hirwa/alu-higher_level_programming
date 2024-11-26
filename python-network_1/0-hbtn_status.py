#!/usr/bin/python3
'''a Python script that fetches a url'''


import urllib.request


url = 'http://0.0.0.0:5050/status'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    '\n    AppleWebKit/537.36 (KHTML, like Gecko)'
    '\n    Chrome/99.0.4844.84 Safari/537.36',
}

req = urllib.request.Request(url, headers=headers)

if __name__ == '__main__':
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
