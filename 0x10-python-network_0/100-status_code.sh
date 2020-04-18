#!/bin/bash
#  This script display only the status code
curl -sI -w "%{http_code}" "$1" -o /dev/null
