import random
import unittest

import convert
import search
import sort
import sums

class Tests(unittest.TestCase):

    def test_convert(self):
        # Base-10 to base-n
        #n = random.randint(1, 16)
        self.assertEqual(convert.base10_to_basen(42, 2),  "101010")
        self.assertEqual(convert.base10_to_basen(42, 3),  "1120")
        self.assertEqual(convert.base10_to_basen(42, 4),  "222")
        self.assertEqual(convert.base10_to_basen(42, 5),  "132")
        self.assertEqual(convert.base10_to_basen(42, 6),  "110")
        self.assertEqual(convert.base10_to_basen(42, 7),  "60")
        self.assertEqual(convert.base10_to_basen(42, 8),  "52")
        self.assertEqual(convert.base10_to_basen(42, 9),  "46")

    def test_search(self):
        # Set up array to search
        array_len = 1024
        max_value = 1024

        # With duplicate values (needs stable binary search)
        #x = sorted([random.randint(0, max_value) for i in range(array_len)])

        # Without duplicate values (doesn't need stable binary search)
        x = range(max_value + 1)
        
        # Pick a random value to search for
        v = random.choice(x)
        idx = x.index(v)

        # Binary search
        # --- value found
        self.assertEqual(search.binary_search(x, v), idx)
        # --- value not found
        self.assertEqual(search.binary_search(x, max_value + 1), -1)

    def test_sort(self):
        # Set up array to sort
        array_len = 1024
        max_value = 1024
        x = [random.randint(0, max_value) for i in range(array_len)]

        # Insertion sort
        self.assertEqual(sort.insertion_sort(x), sorted(x))

        # Merge sort
        self.assertEqual(sort.merge_sort(x), sorted(x))
        
        # Selection sort
        self.assertEqual(sort.selection_sort(x), sorted(x))
        
        # Bubble sort
        self.assertEqual(sort.bubble_sort(x), sorted(x))

        # Heap sort
        self.assertEqual(sort.heap_sort(x), sorted(x))

    def test_sums(self):
        # Set up array to sum
        array_len = 512
        max_value = 512
        x = [random.randint(0, max_value) for i in range(array_len)]

        # Down-by-one recursion
        self.assertEqual(sums.sum_rec_one(x), sum(x))
        # Divide-by-halves recursion
        self.assertEqual(sums.sum_rec_halves(x), sum(x))

if __name__ == '__main__':
    unittest.main()

