#!/bin/bash
# displays the size of body in response field
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then curl -sL "$1"; fi