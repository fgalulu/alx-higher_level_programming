#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as r:
        html = r.read()
        print('{}'.format(html.decode('utf-8')))
