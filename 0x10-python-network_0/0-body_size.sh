#!/bin/bash
# Bash script thattakes in a URL, sends a request to that URL and displays
#the bosy of the response.

curl -so /dev/null "$1" -w '%{size_download}\n'
