#!/bin/bash
#  This script display only the status code
curl -sI "$1" | grep HTTP/1.0 | awk '{ print $2 }'
