#!/bin/bash
#  This script display the methods the server will accept
curl -sI OPTIONS "$1" | grep Allow: | cut -d' ' -f2-
