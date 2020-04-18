#!/bin/bash
#  This script make a request but the response message is You got me!
curl -sL OPTIONS 0.0.0.0:5000/catch_me -X PUT -H "origin: HolbertonSchool" -d "user_id=98"
