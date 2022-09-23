#!/usr/bin/python3
"""
Takes a letter and sends a post request to http with the letter as a prameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    reponse = requests.post(url, data=data)
    try:
        d = response.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
