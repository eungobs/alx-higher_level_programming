#!/usr/bin/python3
"""
requests model
"""

if __name__ == '__main__':
    import requests
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(" - type: {}".format(html.text.__class__))
    print(" - content: {}".format(html.text))
