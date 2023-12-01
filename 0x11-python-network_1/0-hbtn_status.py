#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import urllib.request
import urllib.error

def main():
    """
    Function to print a response of a specific URL
    """
    url = 'https://intranet.hbtn.io/status'
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print('Body response:')
            print(' - type: {}'.format(type(html)))
            print(' - content: {}'.format(html))
            print(' - utf8 content: {}'.format(html.decode('utf-8')))
    except urllib.error.URLError as e:
        print('Error fetching the URL:', e)

if __name__ == "__main__":
    main()
