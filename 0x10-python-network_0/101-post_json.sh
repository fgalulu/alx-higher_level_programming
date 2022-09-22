#!/bin/bash
# script that sends a json POST request to a URL
curl "$1" -sX POST -H "COntent-Type: application/json" -d @"$2"
