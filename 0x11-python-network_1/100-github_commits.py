#!/usr/bin/python3
"""
Github commits code challenge
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}commits".format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()

    for commit in commits:
        i = 0
        while i < 10:
            print(commit)
            print(commit.get('sha'), end=": ")
            print(commit.get('commit').get('author').get('name'))
            i += 1
        break
