#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        answer = response.info()["X-Request-Id"]
        print(answer)
