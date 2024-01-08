#!/bin/bash


if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response=$(curl -sI "$url")

content_length=$(echo "$response" | grep -i "content-length" | awk '{print $2}' | tr -d '\r')

if [ -n "$content_length" ]; then
    echo "Size of the body of the response: ${content_length} bytes"
else
    echo "Content-Length not found in the response headers"
fi
