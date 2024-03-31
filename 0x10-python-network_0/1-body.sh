#!/bin/bash
# Fetches the response body of the given URL if the response code is 200
[ "$(curl -sLI "$1" -X GET | grep "HTTP" | cut -d' ' -f2)" = '200' ] && curl -sL "$1"