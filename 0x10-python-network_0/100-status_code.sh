#!/bin/bash
# This script  displays only the status code of the response.
curl -o "" -sw "%{http_code}" "$1"
