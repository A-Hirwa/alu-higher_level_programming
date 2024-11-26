#!/bin/bash
#finding http methods
curl -s -i -L -X OPTIONS "$1"
