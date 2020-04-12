#!/bin/bash
#  This script display the body size of a website
curl -sI $1 | awk '{ print $NF }' | head -3 | tail -1
