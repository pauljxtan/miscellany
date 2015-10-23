import unittest

import circuits

class Tests(unittest.TestCase):

    def test_half_adder(self):
        self.assertEqual(circuits.half_adder(0, 0), (0, 0))
        self.assertEqual(circuits.half_adder(0, 1), (0, 1))
        self.assertEqual(circuits.half_adder(1, 0), (0, 1))
        self.assertEqual(circuits.half_adder(1, 1), (1, 0))

    def test_full_adder(self):
        self.assertEqual(circuits.full_adder(0, 0, 0), (0, 0))
        self.assertEqual(circuits.full_adder(1, 0, 0), (0, 1))
        self.assertEqual(circuits.full_adder(0, 1, 0), (0, 1))
        self.assertEqual(circuits.full_adder(1, 1, 0), (1, 0))
        self.assertEqual(circuits.full_adder(0, 0, 1), (0, 1))
        self.assertEqual(circuits.full_adder(1, 0, 1), (1, 0))
        self.assertEqual(circuits.full_adder(0, 1, 1), (1, 0))
        self.assertEqual(circuits.full_adder(1, 1, 1), (1, 1))

if __name__ == '__main__':
    unittest.main(verbosity=2)
