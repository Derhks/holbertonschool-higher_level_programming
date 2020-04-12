#!/bin/bash
#  This script display the body size of a website
curl -s $1 -o test | awk '{ print $NF }' test | head -3 | tail -1
