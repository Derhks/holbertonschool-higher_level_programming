#!/usr/bin/python3
"""Show the body of the header response"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        answer = response.read()
        print("\t- type: {}".format(type(answer)))
        print("\t- content: {}".format(answer))
        print("\t- utf8 content: {}".format(answer.decode('utf-8')))
