#!/bin/python3
import argparse
import requests
from bs4 import BeautifulSoup as bs
import os 
import urllib

BEARER_TOKEN = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
URL_ID = "https://api.twitter.com/1.1/guest/activate.json"
URL = 'https://twitter.com/i/api/graphql/gr8Lk09afdgWo7NvzP89iQ/UserByScreenName'


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


def get_headers():
    headers = {
        'authorization': BEARER_TOKEN
    }
    id = requests.post(URL_ID, headers= headers).json()['guest_token']
    
    headers = {
        "authorization": BEARER_TOKEN,
        "x-guest-token": id,
    }
    return headers

def get_params(handle):
    
    # val = f'{"screen_name":{handle},"withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}'
    # e_val  = urllib.parse.quote(val.encode('utf8'))

    # params = {
    #     "variables": f"%7B%22screen_name%22%3A%22{handle}%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D"
    # }
    # params = {
    #     "variables": {
    #         "screen_name": handle
    #     }
    # }
    params = f"variables=%7B%22screen_name%22%3A%22{handle}%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D"
    # print(params)
    return params
                                
def scrap_bio(headers, params):
    # params = {'screen_name': 'elonmusk'}
    # r = requests.get(URL, headers=headers, params=params).json()
    r = requests.get(URL + f"?{params}", headers=headers).json()
    # print(r)
    if r['data']['user']['result']['__typename'] == 'UserUnavailable':
        return "No such user"
    return r['data']['user']['result']['legacy']['description']
    

if __name__ == "__main__":
    handle = get_handle().lower()
    headers = get_headers()
    params = get_params(handle) 
    print(scrap_bio(headers, params))
    