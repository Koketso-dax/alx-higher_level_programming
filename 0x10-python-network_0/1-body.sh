#!/bin/bash
# displays the size of body in response field
curl -s -w "%{http_code}" -o /dev/stderr <URL> | { [ $(tail -n1 /dev/stderr) -eq 200 ] && cat /dev/stdin; }