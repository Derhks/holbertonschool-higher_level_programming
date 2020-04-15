#!/usr/bin/python3
"""What's my status?"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        answer = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(answer)))
        print("\t- content: {}".format(answer))
        print("\t- uft8 content: {}".format(answer.decode("utf-8")))
