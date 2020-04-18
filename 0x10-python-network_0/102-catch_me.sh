#!/bin/bash
#  This script make a request but the response message is You got me!
curl -sL 0.0.0.0:5000/catch_me -o /dev/null -w "You got me!"
