#!/bin/bash
# Use curl to send a request and store the response in a variable

url=$1
curl -sI "$url" | grep -i "content-length" | awk '{print $2}' | tr -d '\r'
