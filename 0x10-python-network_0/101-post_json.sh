#!/bin/bash
#  This script send a JSON POST request
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
