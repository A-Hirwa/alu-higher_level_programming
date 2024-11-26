#!/bin/bash 
# display the body of a file 
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s -L "$1"
