#!/usr/bin/python3
import requests


if __name__ == "__main__":
    webpage = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(webpage.text)))
    print("\t- content: {}".format(webpage.text))
