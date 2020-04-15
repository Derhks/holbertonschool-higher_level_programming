#!/usr/bin/python3
import requests


if __name__ == "__main__":
    webpage = requests.get('https://intranet.hbtn.io')
    print(webpage.headers.get('X-Request-Id'))
