#!/bin/python3

import unittest
from codes.scraper import (
                            save_token, scrap_bio, 
                            get_headers,
                            get_params, BEARER_TOKEN
)

def get_id_header(id):
    headers = {
        "authorization": BEARER_TOKEN,
        "x-guest-token": id,
    }
    return headers

class TestScrapper(unittest.TestCase):
    
    
    def test_token_exist(self):
        handle = "elonmusk"
        headers = get_headers()
        params = get_params(handle) 
        bio_true = scrap_bio(headers, params)
        
        
        id = save_token(save=False)
        header_test = get_id_header(id)
        bio_test = scrap_bio(header_test, params)
        
        self.assertEqual(bio_true, bio_test)


unittest.main()