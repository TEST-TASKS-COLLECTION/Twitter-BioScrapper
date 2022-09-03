#!/bin/python3

import unittest
from codes.scraper import (
                            save_token, scrap_bio, 
                            get_headers,
                            get_params, BEARER_TOKEN
)

HANDLE  = 'elonmus'

# def get_id_header(id):
#     headers = {
#         "authorization": BEARER_TOKEN,
#         "x-guest-token": id,
#     }
#     return headers

class TestScrapper(unittest.TestCase):
    
    def setUp(self):
        id = save_token(save=False)
        header_test = get_headers(err=True)
        # header_test = get_id_header(id)
        params = get_params(HANDLE) 
        self.bio_test = scrap_bio(header_test, params)  
        
    def test_token_exist(self):
        headers = get_headers()
        params = get_params(HANDLE) 
        bio_true = scrap_bio(headers, params)
               
        self.assertEqual(bio_true, self.bio_test)

    def test_type(self):
        self.assertEqual(type(self.bio_test), str)
        
    def test_unavailable(self):
        self.assertNotEqual(self.bio_test, "User Unavailable")
        
    def test_no_such_user(self):
        self.assertNotEqual(self.bio_test, "No Such User")

unittest.main()