import unittest
from unittest.mock import patch
import importlib
import calc_v1

importlib.reload(calc_v1)

from calc_v1 import add, subtract, multiply, divide, remainder, exponent, program

class TestCalcSolution1(unittest.TestCase):
    
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

    @patch("builtins.input", side_effect=["1", "5", "3"])  # Mock user input: choice=1, num1=5, num2=3
    @patch("builtins.print")  # Mock print to capture output
    def test_program_addition(self, mock_print, mock_input):
        program()  # Run the program function
        mock_print.assert_called_with(8)  # Since add(5,3) should return 8, assert this was printed

if __name__ == '__main__':
    unittest.main()