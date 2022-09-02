#!/bin/python3
import argparse
from lib2to3.pgen2 import driver
import platform
from this import d
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

DEVICE = platform.platform().split("-")[0]
SELECTOR = "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div > div > div:nth-child(3) > div > div > span"


def get_handle():
    """
    Returns:
        handle (str): Return the provided handle
    """
    parser = argparse.ArgumentParser(description="A twitter bio scraper")
    parser.add_argument("--handle", help="Twitter handle without the `@`")
    args = parser.parse_args()
    return args.handle


def get_driver_path():
    """
    Returns:
        d_path (str): return the driver path
    """
    if DEVICE == "Linux":
        d_path = r"data/geckodriver"
    elif DEVICE == "Windows":
        d_path = r"data/win64/geckodriver.exe"
        
    return d_path

def scrap_bio(d_path, url):
    option = webdriver.FirefoxOptions()
    option.headless = True
    # option.add_argument('headless')
    driver = webdriver.Firefox(executable_path=d_path, options=option)
    
    driver.get(url)
    
    bio = driver.find_element("css selector", SELECTOR)
    
    return bio.text
    
    

if __name__ == "__main__":
    handle = get_handle()
    
    url = f"https://twitter.com/{handle}"
    
    d_path = get_driver_path()
    
    print(scrap_bio(d_path, url))
    