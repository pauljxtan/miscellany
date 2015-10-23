import unittest

import gates

class Tests(unittest.TestCase):

    def test_AND(self):
        self.assertEqual(gates.AND(0, 0), 0)
        self.assertEqual(gates.AND(0, 1), 0)
        self.assertEqual(gates.AND(1, 0), 0)
        self.assertEqual(gates.AND(1, 1), 1)

    def test_AND3(self):
        self.assertEqual(gates.AND3(0, 0, 0), 0)
        self.assertEqual(gates.AND3(0, 0, 1), 0)
        self.assertEqual(gates.AND3(0, 1, 0), 0)
        self.assertEqual(gates.AND3(0, 1, 1), 0)
        self.assertEqual(gates.AND3(1, 0, 0), 0)
        self.assertEqual(gates.AND3(1, 0, 1), 0)
        self.assertEqual(gates.AND3(1, 1, 0), 0)
        self.assertEqual(gates.AND3(1, 1, 1), 1)

    def test_AND4(self):
        self.assertEqual(gates.AND4(0, 0, 0, 0), 0)
        self.assertEqual(gates.AND4(0, 0, 0, 1), 0)
        self.assertEqual(gates.AND4(0, 0, 1, 0), 0)
        self.assertEqual(gates.AND4(0, 0, 1, 1), 0)
        self.assertEqual(gates.AND4(0, 1, 0, 0), 0)
        self.assertEqual(gates.AND4(0, 1, 0, 1), 0)
        self.assertEqual(gates.AND4(0, 1, 1, 0), 0)
        self.assertEqual(gates.AND4(0, 1, 1, 1), 0)
        self.assertEqual(gates.AND4(1, 0, 0, 0), 0)
        self.assertEqual(gates.AND4(1, 0, 0, 1), 0)
        self.assertEqual(gates.AND4(1, 0, 1, 0), 0)
        self.assertEqual(gates.AND4(1, 0, 1, 1), 0)
        self.assertEqual(gates.AND4(1, 1, 0, 0), 0)
        self.assertEqual(gates.AND4(1, 1, 0, 1), 0)
        self.assertEqual(gates.AND4(1, 1, 1, 0), 0)
        self.assertEqual(gates.AND4(1, 1, 1, 1), 1)

    def test_OR(self):
        self.assertEqual(gates.OR(0, 0), 0)
        self.assertEqual(gates.OR(0, 1), 1)
        self.assertEqual(gates.OR(1, 0), 1)
        self.assertEqual(gates.OR(1, 1), 1)

    def test_OR4(self):
        self.assertEqual(gates.OR4(0, 0, 0, 0), 0)
        self.assertEqual(gates.OR4(0, 0, 0, 1), 1)
        self.assertEqual(gates.OR4(0, 0, 1, 0), 1)
        self.assertEqual(gates.OR4(0, 0, 1, 1), 1)
        self.assertEqual(gates.OR4(0, 1, 0, 0), 1)
        self.assertEqual(gates.OR4(0, 1, 0, 1), 1)
        self.assertEqual(gates.OR4(0, 1, 1, 0), 1)
        self.assertEqual(gates.OR4(0, 1, 1, 1), 1)
        self.assertEqual(gates.OR4(1, 0, 0, 0), 1)
        self.assertEqual(gates.OR4(1, 0, 0, 1), 1)
        self.assertEqual(gates.OR4(1, 0, 1, 0), 1)
        self.assertEqual(gates.OR4(1, 0, 1, 1), 1)
        self.assertEqual(gates.OR4(1, 1, 0, 0), 1)
        self.assertEqual(gates.OR4(1, 1, 0, 1), 1)
        self.assertEqual(gates.OR4(1, 1, 1, 0), 1)
        self.assertEqual(gates.OR4(1, 1, 1, 1), 1)

    def test_NOT(self):
        self.assertEqual(gates.NOT(0), 1)
        self.assertEqual(gates.NOT(1), 0)

    def test_NAND(self):
        self.assertEqual(gates.NAND(0, 0), 1)
        self.assertEqual(gates.NAND(0, 1), 1)
        self.assertEqual(gates.NAND(1, 0), 1)
        self.assertEqual(gates.NAND(1, 1), 0)

    def test_NOR(self):
        self.assertEqual(gates.NOR(0, 0), 1)
        self.assertEqual(gates.NOR(0, 1), 0)
        self.assertEqual(gates.NOR(1, 0), 0)
        self.assertEqual(gates.NOR(1, 1), 0)

    def test_XOR(self):
        self.assertEqual(gates.XOR(0, 0), 0)
        self.assertEqual(gates.XOR(0, 1), 1)
        self.assertEqual(gates.XOR(1, 0), 1)
        self.assertEqual(gates.XOR(1, 1), 0)

    def test_XNOR(self):
        self.assertEqual(gates.XNOR(0, 0), 1)
        self.assertEqual(gates.XNOR(0, 1), 0)
        self.assertEqual(gates.XNOR(1, 0), 0)
        self.assertEqual(gates.XNOR(1, 1), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

