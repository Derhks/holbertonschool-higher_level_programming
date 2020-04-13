#!/bin/bash
#  This script send a POST request
curl -X POST "$1" -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
