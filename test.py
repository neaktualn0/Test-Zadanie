import unittest
import start
from dotenv import load_dotenv
from os import getenv

load_dotenv()
file = getenv("DATA_TEST_JSON_PATH")


class OutputTesting(unittest.TestCase):
    def test_output(self):
        res = start.output(1)
        self.assertEqual(type(res), str)
    
    def test_add(self):
        res = start.add('','','','','')
        self.assertEqual(type(res), str)


        
        
     