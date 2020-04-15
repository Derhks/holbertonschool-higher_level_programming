#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        answer = response.read()
        print("Body response:")
        print("    - type: {}".format(type(answer)))
        print("    - content: {}".format(answer))
        print("    - uft8 content: {}".format(answer.decode("utf-8")))