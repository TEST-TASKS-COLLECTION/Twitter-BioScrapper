#!/bin/python3
import argparse
import requests
from bs4 import BeautifulSoup as bs
import os 
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

def get_handle():
    """
    Returns:
        handle (str): Return the provided handle
    """
    parser = argparse.ArgumentParser(description="A twitter bio scraper")
    parser.add_argument("--handle", help="Twitter handle without the `@`")
    args = parser.parse_args()
    return args.handle



def scrap_bio(url):
    r = requests.get(url, headers=headers).json()
    # print(r)
    if r['errors']:
        return "No such user"
    return r['data'][0]['description']
    

if __name__ == "__main__":
    handle = get_handle()
    url = f"https://api.twitter.com/2/users/by?user.fields=description&usernames={handle}"    
    print(scrap_bio(url))
    