#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    Funtion to print a response of a specific url
    """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print(' - type: {}'.format(type(html)))
        print(' - content: {}'.format(html))
        print(' - utf8 content: {}'.format(html.decode('utf8')))

if __name__ == "__main__":
    main()
