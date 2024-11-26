#!/bin/bash 
# display the body of a file 
curl -s -o /dev/null -w "%{http_code}" -L "$1" | grep -q "^200$" && curl -s -L "$1"
