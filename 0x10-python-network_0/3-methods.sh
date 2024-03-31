#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sI --head "$1" | grep -i Allow
