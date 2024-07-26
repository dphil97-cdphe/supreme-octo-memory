# tests/test_download_1.py

import unittest
from pathlib import Path
from ex_1_download.ex_1_download import is_valid_url, create_paths

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

class TestCreatePaths(unittest.TestCase):
    pass

class Test
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIsValidUrl))
    suite.addTest(unittest.makeSuite(TestCreatePaths))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())