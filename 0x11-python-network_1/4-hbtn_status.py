#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using the requests package
"""
import requests

def main():
    """
    Function to fetch and display the body response in the required format
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    
    print('Body response:')
    print('\t- type:', type(response.text))
    print('\t- content:', response.text)

if __name__ == "__main__":
    main()
