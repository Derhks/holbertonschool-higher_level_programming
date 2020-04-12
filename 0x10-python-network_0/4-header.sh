#!/bin/bash
#  script that send a GET request and display de body
curl -sL "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
