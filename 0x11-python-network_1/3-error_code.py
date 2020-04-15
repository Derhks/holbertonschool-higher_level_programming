#!/usr/bin/python3
import urllib.request
import sys


if __name__ == "__main__":
        try:
            request = urllib.request.Request(sys.argv[1])
            with urllib.request.urlopen(request) as response:
                print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as error:
            print("Error code: {:d}".format(error.code))
