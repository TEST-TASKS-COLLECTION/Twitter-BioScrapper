#!/bin/python3

import unittest
from codes.scraper import (
                            save_token, scrap_bio, 
                            get_headers,
                            get_params, BEARER_TOKEN
)
import os

HANDLE  = 'elonmusk'
# HANDLE  = 'elonmus'
# HANDLE  = 'mikey19xx'
SAVE_FILE = 'guest_id.txt'

class TestScrapper(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        # id = get_id(err=True)
        # header_test = get_headers(err=True)
        # header_test = get_id_header(id)
        print("TEST TOKEN", save_token(save=True))
        self.bio_test = scrap_bio(HANDLE)  
        
    def test_token_exist(self):
        bio_true = scrap_bio(HANDLE)
        self.assertEqual(bio_true, self.bio_test)

    def test_type(self):
        self.assertEqual(type(self.bio_test), str)
        
    def test_unavailable(self):
        self.assertNotEqual(self.bio_test, "User Unavailable")
        
    def test_no_such_user(self):
        self.assertNotEqual(self.bio_test, "No Such User")
        
    def test_file_created(self):
        os.remove(f"data/{SAVE_FILE}")
        _ = save_token()
        self.assertIn(SAVE_FILE, os.listdir('data'))

unittest.main()