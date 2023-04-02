#!/bin/bash
# This script send a POST request with the contents of a file.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
