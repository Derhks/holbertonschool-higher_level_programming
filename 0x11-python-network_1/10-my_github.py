#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
        my = requests.get('https://api.github.com/user',
                          auth=(sys.argv[1], sys.argv[2]))
        print(my.json().get('id'))
