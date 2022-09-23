#!/usr/bin/python3
"""
Takes url and sends a request to the url and displays the bosy of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
