import unittest
from Estructuras.PruebasUnitarias.codigo import invert_string


class TestFactorial(unittest.TestCase):
    def test_one_digit(self):
        # Arrange
        n = "n"
        expected = "n"

        # Act
        result = invert_string(n)

        # Assert
        self.assertEqual(result, expected)

    def test_no_letters(self):
        self.assertEqual(invert_string(""),"")

    def test_normal_string(self):
        self.assertEqual(invert_string("hola"), "aloh")