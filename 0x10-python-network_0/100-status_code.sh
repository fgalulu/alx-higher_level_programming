#!/bin/bash
# script that sends a request to a URL passed as an arguement.
curl "$1" -w '%{http_code}' -so /dev/null
