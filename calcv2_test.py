import unittest
from unittest.mock import patch
import importlib
import calc_v2

importlib.reload(calc_v2)

from calc_v2 import add, subtract, multiply, divide, remainder, exponent, program

class TestCalcSolution2(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(-1, 1), 0)
        self.assertEqual(remainder(-1, -1), 0)

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(-1, 1), -1)
        self.assertEqual(exponent(-1, -1), -1)

    @patch("builtins.input", side_effect=["1", "5", "3", "no"])  # Simulate: choice=1, num1=5, num2=3, exit program
    @patch("builtins.print")  # Mock print output
    def test_program_addition(self, mock_print, mock_input):
        program()  # Run the program function
        mock_print.assert_any_call(8)  # Expect output of 5 + 3 = 8

    @patch("builtins.input", side_effect=["4", "10", "2", "no"])  # Simulate: choice=4, num1=10, num2=2, exit
    @patch("builtins.print")  # Mock print output
    def test_program_division(self, mock_print, mock_input):
        program()  # Run the program function
        mock_print.assert_any_call(5)  # Expect output of 10 / 2 = 5

    @patch("builtins.input", side_effect=["6", "2", "3", "yes", "5", "10", "3", "no"])  
    @patch("builtins.print")  
    def test_program_exponent_and_remainder(self, mock_print, mock_input):
        program()  
        mock_print.assert_any_call(8)  # Expect 2^3 = 8
        mock_print.assert_any_call(1)  # Expect 10 % 3 = 1

if __name__ == "__main__":
    unittest.main()
