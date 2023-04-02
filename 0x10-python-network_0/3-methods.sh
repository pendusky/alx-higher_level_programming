#!/bin/bash
# This script displays all HTTP methods the server will accept.
curl -sI "$1" | awk -F": " '/^Allow/{print $2}'
