#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    webpage = requests.get(sys.argv[1])
    print(webpage.headers.get('X-Request-Id'))
