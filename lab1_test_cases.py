import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([1,2,5,67]), 67)
        self.assertEqual(max_list_iter([1]), 1)

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
           reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3 )
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 5)
        self.assertEqual(bin_search(4, 3, 2, list_val), None)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
           bin_search(4, 0, 5, tlist)
if __name__ == "__main__":
        unittest.main()

    
