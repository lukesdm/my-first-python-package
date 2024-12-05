import lukepy
import unittest

class TestLuke(unittest.TestCase):
    
    def test_random_list(self):
        r = lukepy.random_list(6)
        self.assertIsInstance(r, list)
