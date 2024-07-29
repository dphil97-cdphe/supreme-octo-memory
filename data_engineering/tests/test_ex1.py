# tests/test_download_1.py

import unittest

import sys
sys.path.append("..")

from src.ex1 import is_valid_url


"""
Each class tests a function
Each method within that class tests a scenario handled by that function
"""

VALID_URL = "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip"
INVALID_URL = "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2099_Q5.zip"

class TestIsValidUrl(unittest.TestCase):
    def test_valid_url(self):
        result = is_valid_url(VALID_URL)
        self.assertTrue(result)

    def test_invalid_url(self):
        result = is_valid_url(INVALID_URL)
        self.assertFalse(result)
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIsValidUrl))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())