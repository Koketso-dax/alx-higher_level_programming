#!/bin/bash
# displays the size of body in response field
response_code=$(curl -sLI "$1" -X GET | grep "HTTP" | cut -d' ' -f2)
if [ "$response_code" = '200' ]; then
    curl -sL "$1"
fi