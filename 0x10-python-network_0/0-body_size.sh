#!/bin/bash

if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi

response=$(curl -s -o /dev/null -w "%{size_download}" "$1")
echo "Size of the response body: $response bytes"

