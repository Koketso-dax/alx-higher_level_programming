#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-