# tests/test_download_1.py

import unittest
from my_script import add

"""
what to test
- invalid url is not processed
- ensure downloads/ exists
- ensure file is unzipped
- ensure original file is deleted
"""


class TestProcessFileFunction(unittest.TestCase):
    def test_process_file(self):
        pass