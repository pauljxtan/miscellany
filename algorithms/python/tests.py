import random
import unittest

import search
import sort

class Tests(unittest.TestCase):

    def test_search(self):
        # Set up array to search
        array_len = 1000
        max_value = 1000

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
        array_len = 1000
        max_value = 1000
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


if __name__ == '__main__':
    unittest.main()

