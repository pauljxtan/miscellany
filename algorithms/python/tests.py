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
        self.assertEqual(convert.base10_to_basen(42, 2), '101010')
        self.assertEqual(convert.base10_to_basen(42, 3), '1120')
        self.assertEqual(convert.base10_to_basen(42, 5), '132')
        self.assertEqual(convert.base10_to_basen(42, 8), '52')
        self.assertEqual(convert.base10_to_basen(42, 12), '36')
        self.assertEqual(convert.base10_to_basen(42, 17), '28')
        self.assertEqual(convert.base10_to_basen(42, 23), '1j')
        self.assertEqual(convert.base10_to_basen(42, 30), '1c')

    def test_search(self):
        # Set up array to search
        array_len = 1024
        max_value = 1024

        # With duplicate values (needs stable binary search)
        #x = sorted([random.randint(0, max_value) for i in range(array_len)])

        # Without duplicate values (doesn't need stable binary search)
        x = range(max_value + 1)
        
        # Pick a random value to search for
        v = random.choice(x[1:-1])
        idx = x.index(v)

        # Binary search
        # --- value found
        self.assertEqual(search.binary_search(x, v), idx)
        # (Edge cases)
        self.assertEqual(search.binary_search(x, x[0]), 0)
        self.assertEqual(search.binary_search(x, x[array_len - 1]), array_len - 1)
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
        # Going-up recursion
        self.assertEqual(sums.sum_rec_goingup(x, 0, array_len - 1), sum(x))
        # Going-down recursion
        self.assertEqual(sums.sum_rec_goingdown(x, 0, array_len - 1), sum(x))

if __name__ == '__main__':
    unittest.main(verbosity=2)

