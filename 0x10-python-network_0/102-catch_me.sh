#!/bin/bash
# script that makes a request to 0.0.0.0:500/catch_me
curl -sLH "Origin: School" -d "user_id=98" -X PUT 0:5000/catch_me
