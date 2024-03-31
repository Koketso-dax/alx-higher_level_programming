#!/bin/bash
# Fetches the body of the response for a given URL if the response status code is 200
curl -s -L -o /tmp/response_body -w "%{http_code}" --max-redirs 5 "$1" | { [ "$(tail -n1 /tmp/response_body)" -eq 200 ] && cat /tmp/response_body; }
