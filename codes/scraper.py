#!/bin/python3
import argparse
import requests
from bs4 import BeautifulSoup as bs
import os 
import urllib
import json

BEARER_TOKEN = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
URL_ID = "https://api.twitter.com/1.1/guest/activate.json"
URL = 'https://twitter.com/i/api/graphql/gr8Lk09afdgWo7NvzP89iQ/UserByScreenName'



def get_handle():
    """
    Returns:
        handle (str): Return the provided handle
    """
    parser = argparse.ArgumentParser(description="A twitter bio scraper")
    parser.add_argument("--handle", help="Twitter handle without the `@`")
    args = parser.parse_args()
    return args.handle


def get_id(err=True):
    """
    Args:
        err (bool, optional): If error generate a new id. Defaults to False.

    Returns:
        id (str): return the generated id
    """
    try:
        if err:
            # print("CREATING NEW TOKEN")
            id = save_token()
        
        else:
            # print("USING CACHE")
            id = read_token()
            
            if not id:
                return get_headers(err=True)
    except FileNotFoundError:
        return get_headers(err=True)
    
    return id

def get_headers(id):
    """
    Args:
        id (str): the twitter generated id

    Returns:
        headers (dict): dict with bearer token and id as values
    """

    
    headers = {
        "authorization": BEARER_TOKEN,
        "x-guest-token": id,
    }
    # print(headers)
    return headers

def read_token():
    # print("READING TOKEN FORM FILE")
    with open('data/guest_id.txt', "r") as f:
        id = f.read()
    # print("ID IS:", id)
    return id

def save_token(save=True):
    """
    Return:
        id (str): a token generated from twitter 
    """
    headers = {
        "Authorization": f"{BEARER_TOKEN}"
    }
    id = requests.post(URL_ID, headers= headers).json()['guest_token']
    # id = requests.post(URL_ID, headers= headers).json()
    # print(id)
    if save:
        with open('data/guest_id.txt', "w") as f:
            f.write(id)
    return id

def get_params(handle):
    """

    Args:
        handle (str): a twitter user handle 

    Returns:
        params (dict): params to pass into the request 
    """
    val = {"screen_name": f"{handle}","withSafetyModeUserFields":True,"withSuperFollowsUserFields":True}
    params = {
        "variables" : json.dumps(val)
    }
    return params
                                
def scrap_bio(headers, params):
    """

    Args:
        headers (_type_): _description_
        params (_type_): _description_

    Returns:
        - returns a user bio if user exists
        - provide feedback if there is no user or they are not available
    """
    r = requests.get(URL, headers=headers, params=params).json()
    # print(r)
    try:
        if r.get('errors', False):
            # print("WRNG GUEST TOKEN")
            headers = get_headers(err=True)
            return scrap_bio(headers, params)
        if r['data']['user']['result']['__typename'] == 'UserUnavailable':
            return "User Unavailable"
        return r['data']['user']['result']['legacy']['description']
    except KeyError:
        return "No Such User"
    # except json.JSONDecodeError:
    #     return scrap_bio(headers, params)
    

if __name__ == "__main__":
    handle = get_handle().lower()
    # handle = "elonmusk"
    id = get_id()
    headers = get_headers(id)
    params = get_params(handle) 
    print(scrap_bio(headers, params))
    