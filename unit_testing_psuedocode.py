import unittest
from unit_testing_lab import add

## Unit Tests for psuedocode

class TestFunction(unittest.TestCase):
    

    def test_add(self):
        result = add(5)
        self.assertEqual(result,6)
    
if __name__ == '__main__':
    unittest.main()