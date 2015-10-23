import itertools
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

    def test_multiplexer_2to1(self):
        for (S, A, B) in itertools.product((0, 1), repeat=3):
            if S == 0:
                self.assertEqual(circuits.multiplexer_2to1(S, A, B), A)
            else:
                self.assertEqual(circuits.multiplexer_2to1(S, A, B), B)

        # Test enable=0 (active high)
        for (S, A, B) in itertools.product((0, 1), repeat=3):
            self.assertEqual(circuits.multiplexer_2to1(S, A, B, 0), 0)

    def test_multiplexer_4to1(self):
        for (S_0, S_1, A, B, C, D) in itertools.product((0, 1), repeat=6):
            if S_1 == 0 and S_0 == 0:
                self.assertEqual(circuits.multiplexer_4to1(S_0, S_1, A, B, C, D), A)
            elif S_1 == 0 and S_0 == 1:
                self.assertEqual(circuits.multiplexer_4to1(S_0, S_1, A, B, C, D), B)
            elif S_1 == 1 and S_0 == 0:
                self.assertEqual(circuits.multiplexer_4to1(S_0, S_1, A, B, C, D), C)
            else:
                self.assertEqual(circuits.multiplexer_4to1(S_0, S_1, A, B, C, D), D)

        # Test enable=0 (active high)
        for (S_0, S_1, A, B, C, D) in itertools.product((0, 1), repeat=6):
            self.assertEqual(circuits.multiplexer_4to1(S_0, S_1, A, B, C, D, 0), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
