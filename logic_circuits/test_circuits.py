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
        for (I_1, I_0, S) in itertools.product((0, 1), repeat=3):
            if S == 0:
                self.assertEqual(circuits.multiplexer_2to1(I_1, I_0, S), I_0)
            else:
                self.assertEqual(circuits.multiplexer_2to1(I_1, I_0, S), I_1)

        # Test enable=0 (active high)
        for (S, I_1, I_0) in itertools.product((0, 1), repeat=3):
            self.assertEqual(circuits.multiplexer_2to1(S, I_1, I_0, E=0), 0)

    def test_multiplexer_4to1(self):
        for (I_3, I_2, I_1, I_0, S_1, S_0) in itertools.product((0, 1), repeat=6):
            if S_1 == 0 and S_0 == 0:
                self.assertEqual(circuits.multiplexer_4to1(I_3, I_2, I_1, I_0, S_1, S_0), I_0)
            elif S_1 == 0 and S_0 == 1:                                                
                self.assertEqual(circuits.multiplexer_4to1(I_3, I_2, I_1, I_0, S_1, S_0), I_1)
            elif S_1 == 1 and S_0 == 0:                                                
                self.assertEqual(circuits.multiplexer_4to1(I_3, I_2, I_1, I_0, S_1, S_0), I_2)
            else:                                                                      
                self.assertEqual(circuits.multiplexer_4to1(I_3, I_2, I_1, I_0, S_1, S_0), I_3)

        # Test enable=0 (active high)
        for (I_3, I_2, I_1, I_0, S_1, S_0) in itertools.product((0, 1), repeat=6):
            self.assertEqual(circuits.multiplexer_4to1(I_3, I_2, I_1, I_0, S_1, S_0, E=0), 0)

    def test_demultiplexer_1to4(self):
        for (I, S_1, S_0) in itertools.product((0, 1), repeat=3):
            if S_1 == 0 and S_0 == 0:
                self.assertEqual(circuits.demultiplexer_1to4(I, S_1, S_0)[3-0], I)
            elif S_1 == 0 and S_0 == 1:
                self.assertEqual(circuits.demultiplexer_1to4(I, S_1, S_0)[3-1], I)
            elif S_1 == 1 and S_0 == 0:
                self.assertEqual(circuits.demultiplexer_1to4(I, S_1, S_0)[3-2], I)
            else:
                self.assertEqual(circuits.demultiplexer_1to4(I, S_1, S_0)[3-3], I)

    def test_encoder_4to2(self):
        self.assertEqual(circuits.encoder_4to2(0, 0, 0, 1), (0, 0))
        self.assertEqual(circuits.encoder_4to2(0, 0, 1, 0), (0, 1))
        self.assertEqual(circuits.encoder_4to2(0, 1, 0, 0), (1, 0))
        self.assertEqual(circuits.encoder_4to2(1, 0, 0, 0), (1, 1))

    def test_decoder2to4(self):
        self.assertEqual(circuits.decoder_2to4(0, 0), (0, 0, 0, 1))
        self.assertEqual(circuits.decoder_2to4(0, 1), (0, 0, 1, 0))
        self.assertEqual(circuits.decoder_2to4(1, 0), (0, 1, 0, 0))
        self.assertEqual(circuits.decoder_2to4(1, 1), (1, 0, 0, 0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
