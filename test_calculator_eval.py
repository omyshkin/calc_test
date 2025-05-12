import unittest
from calculator_eval import evaluate_expression

class TestEvalCalculator(unittest.TestCase):

    def test_basic_operations(self):
        self.assertEqual(evaluate_expression("2 + 2"), 4)
        self.assertEqual(evaluate_expression("-1 + 1"), 0)
        self.assertEqual(evaluate_expression("-1 + -1"), -2)
        self.assertEqual(evaluate_expression("10 - 5"), 5)
        self.assertEqual(evaluate_expression("2 - 5"), -3)
        self.assertEqual(evaluate_expression("-1 - -1"), 0)
        self.assertEqual(evaluate_expression("3 * 4"), 12)
        self.assertEqual(evaluate_expression("4 * 3"), 12)
        self.assertEqual(evaluate_expression("-1 * 1"), -1)
        self.assertEqual(evaluate_expression("0 * 5"), 0)
        self.assertEqual(evaluate_expression("12 / 4"), 3)
        self.assertEqual(evaluate_expression("5 / 2"), 2.5)
        self.assertEqual(evaluate_expression("-1 / 2"), -0.5)
        self.assertEqual(evaluate_expression("1 / -2"), -0.5)
        self.assertEqual(evaluate_expression("11"), 11)

    def test_large_numbers(self):
        self.assertEqual(evaluate_expression("1342934298 / 2"), 671467149.0)
        self.assertEqual(evaluate_expression("438 + 2387879 * 3332334"), 7957210380024)

    def test_unary_operations(self):
        self.assertEqual(evaluate_expression("++2349037"), 2349037)
        self.assertEqual(evaluate_expression("-+739.3094"), -739.3094)

    def test_octal(self):
        self.assertEqual(evaluate_expression("0o10 + 2"), 10)  # Octal representation

    def test_floating_point_and_integers(self):
        self.assertAlmostEqual(evaluate_expression("3.14 + 2"), 5.14, places=5)
        self.assertAlmostEqual(evaluate_expression("1.5 * 2.5"), 3.75, places=5)

    def test_invalid_expressions(self):
        self.assertEqual(evaluate_expression("2 + (3 * 4"), "'(' was never closed (<string>, line 1)")
        self.assertEqual(evaluate_expression("2 + 3 * "), "invalid syntax (<string>, line 1)")
        self.assertEqual(evaluate_expression("1342934298/"), "invalid syntax (<string>, line 1)")
        self.assertEqual(evaluate_expression("++2349037*"), "invalid syntax (<string>, line 1)")
        self.assertEqual(evaluate_expression("00011"), "leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers (<string>, line 1)")
        self.assertEqual(evaluate_expression("2 / 0"), "division by zero")
        self.assertEqual(evaluate_expression("abc + 1"), "name 'abc' is not defined")

    def test_complex_expressions(self):
        self.assertEqual(evaluate_expression("1 + 2 * (3 + 4)"), 15)
        self.assertEqual(evaluate_expression("((5 - 2) * (8 + 1)) / 3"), 9.0)

    def test_overflow_simulation(self):
        # Simulate a very large number computation
        large_number_expr = "10**1000"  # A very large number
        result = evaluate_expression(large_number_expr)
        self.assertTrue(result > 0)

        # Testing large calculations that should not raise an error
        self.assertEqual(evaluate_expression("10**100 + 10**100"), 2 * (10**100))

        # Testing a case that could lead to excessive computation
        # (This is more of an educational example; actual overflow won't occur in Python)
        overflow_expr = "2**100000"  # Extremely large computation
        result = evaluate_expression(overflow_expr)
        self.assertTrue(isinstance(result, int))

if __name__ == '__main__':
    unittest.main()
