#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    post = ""
    if len(sys.argv) == 2:
        post = sys.argv[1]
    try:
        webpage = requests.post('http://0.0.0.0:5000/search_user',
                                data={'q': post})
        if len(webpage.text) < 4:
            print("No result")
        if webpage.json():
            print("[{}] {}".format(webpage.json().get('id'),
                                   webpage.json().get('name')))
    except:
        print("Not a valid JSON")
