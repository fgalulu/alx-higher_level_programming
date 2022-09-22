#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and display response
curl "$1" -s -X POST -d "email=test@gamil.com&subject=I will always be here for PLD"
