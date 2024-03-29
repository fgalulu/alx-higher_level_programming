#!/usr/bin/python3
"""
python script taht takes in url, sends a request to the url and
displays the body of the response.
"""

import urllib.request as request
import urllib.parse as parse
from urllib import error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
