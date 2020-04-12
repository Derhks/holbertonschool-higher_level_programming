#!/bin/bash
#  This script display the body size of a website
curl -sI "$1" | grep Content-Length: | awk '{ print $2 }'
