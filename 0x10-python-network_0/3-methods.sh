#!/bin/bash
#  This script display the methods the server will accept
curl -sI -X OPTIONS "$1" | grep Allow: | cut -f 2-4 -d" "
