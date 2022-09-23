#!/usr/bin/python3
"""
Python script that takes in a url, sends a request to the url and
diplays the value of the X-Request-Id
"""

import urllib.request as request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as r:
        print(r.getheader("x-Request-Id"))
