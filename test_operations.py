import unittest

class TestArithmeticOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 2, 3)
        self.assertEqual(-1 + 1, 0)
        self.assertEqual(-1 + -1, -2)

    def test_subtract(self):
        self.assertEqual(5 - 3, 2)
        self.assertEqual(2 - 5, -3)
        self.assertEqual(-1 - -1, 0)

    def test_multiply(self):
        self.assertEqual(3 * 4, 12)
        self.assertEqual(-1 * 1, -1)
        self.assertEqual(0 * 5 , 0)

    def test_divide(self):
        self.assertEqual(10 / 2, 5)
        self.assertEqual(5 / 2, 2.5)
        self.assertEqual(-1 / 2, -0.5)
        self.assertEqual(1 / -2, -0.5)
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0  # Check Zero Division

    def test_large_numbers(self):
        self.assertEqual(1e100 + 1e100, 2e100)
        self.assertEqual(1e308 * 1e10, float('inf'))  # Check for overflow

if __name__ == '__main__':
    unittest.main()
