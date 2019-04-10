import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location(SLO, 35.3, -120.7)")
    def test_eq(self):
    	loc1 = Location("SLO", 35.3, -120.7)
    	loc2 = Location("Paris", 48.9, 2.4)
    	loc3 = Location("SLO", 35.3, -120.7)
    	self.assertEqual((loc1 == loc2), False)
    	self.assertEqual((loc1 == loc3), True)

    # Add more tests!

if __name__ == "__main__":
        unittest.main()
