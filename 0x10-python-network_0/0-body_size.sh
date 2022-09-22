#!/bin/bash
# Bash script thattakes in a URL, sends a request to that URL and displays
#the bosy of the response.

curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2
