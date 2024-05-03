import unittest
from main.logica import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        apps_to_dict()
        self.assertNotEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
