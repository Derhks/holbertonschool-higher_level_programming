#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    mail = urllib.parse.urlencode({'email': sys.argv[2]})
    mail_encode = mail.encode('ascii')
    request = urllib.request.Request(sys.argv[1], mail_encode)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
