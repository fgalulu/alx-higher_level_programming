#!/bin/bash
# script tah takes in a URL, sends a GET request, displays the body of resp.
curl -s -H "X-School-User-Id: 98" -X GET "$1"
