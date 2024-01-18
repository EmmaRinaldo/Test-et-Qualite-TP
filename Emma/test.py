# test.py
import unittest
from main import calculate



class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculate("4 + 2")
        self.assertEqual(result, 6)

    def test_subtraction(self):
        result = calculate("4 - 2")
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = calculate("4 * 2")
        self.assertEqual(result, 8)

    def test_division(self):
        result = calculate("8 / 2")
        self.assertEqual(result, 4)

    def test_exponentiation(self):
        result = calculate("2 ^ 3")
        self.assertEqual(result, 8)

    def test_modulo(self):
        result = calculate("5 % 2")
        self.assertEqual(result, 1)

    def test_complex_expression(self):
        result = calculate("5 + 5 % 2 - 3")
        self.assertEqual(result, -3)

    def test_invalid_expression(self):
        with self.assertRaises(Exception):
            calculate("4 +")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("5 / 0")

    # Add more test cases based on the specified requirements and edge cases

if __name__ == "__main__":
    unittest.main()

