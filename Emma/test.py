# test.py
import unittest
from main import MathOperations

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        result = MathOperations.evaluate_expression("2 + 3")
        self.assertEqual(result, 5)

    def test_soustraction(self):
        result = MathOperations.evaluate_expression("5 - 3")
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = MathOperations.evaluate_expression("2 * 3")
        self.assertEqual(result, 6)

    def test_division(self):
        result = MathOperations.evaluate_expression("6 / 3")
        self.assertEqual(result, 2)

    def test_complex_expression(self):
        result = MathOperations.evaluate_expression("2 + 3 * 4 - 2")
        self.assertEqual(result, 12)

    def test_expression_with_negative_numbers(self):
        result = MathOperations.evaluate_expression("2 - 5 + (-3)")
        self.assertEqual(result, -6)

    def test_expression_with_float_numbers(self):
        result = MathOperations.evaluate_expression("1.5 * 2")
        self.assertEqual(result, 3.0)

    def test_expression_with_parentheses(self):
        result = MathOperations.evaluate_expression("(2 + 3) * 4")
        self.assertEqual(result, 20)

    def test_expression_with_power(self):
        result = MathOperations.evaluate_expression("2 ^ 3")
        self.assertEqual(result, 8)

    def test_expression_with_mixed_operations(self):
        result = MathOperations.evaluate_expression("2 + 3 * (4 - 2) / 2")
        self.assertEqual(result, 5)

