#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    webpage = requests.get(sys.argv[1])
    if webpage:
        print(webpage.text)
    if webpage.status_code >= 400:
        print("Error code: {:d}".format(webpage.status_code))
