#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using the urllib package and with statement
"""
import urllib.request

def main():
    """
    Function to fetch and display the body response in the required format using urllib and with statement
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)

if __name__ == "__main__":
    main()
