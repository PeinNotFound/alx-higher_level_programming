#!/bin/bash
# This script takes in a URL, sends a request to that URL using curl, and displays the size of the body of the response in bytes.

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL using curl, silence output, and count bytes of the response body
curl_output=$(curl -sI "$1")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Failed to fetch URL: $1"
    exit 1
fi

# Extract the content length from the response headers and display it
content_length=$(echo "$curl_output" | grep -i Content-Length | awk '{print $2}')

# Check if content length was found
if [ -z "$content_length" ]; then
    echo "Failed to determine content length"
    exit 1
fi

echo "$content_length"
