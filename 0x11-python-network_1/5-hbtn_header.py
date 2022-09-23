#!/usr/bin/python3
"""
script that takes a url, sends a request to the url and displays the value
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
