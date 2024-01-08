#!/bin/bash
# Use curl to send a request and store the response in a variable
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
