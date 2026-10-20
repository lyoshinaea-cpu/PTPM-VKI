import unittest

from src.calculator import TriangleCalculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = TriangleCalculator()

    def test_non_numeric_sides(self):
        result = self.calculator.calculate("abc", "4", "5")

        self.assertEqual(
            result,
            (None, "Стороны должны быть числами")
        )

    def test_negative_sides(self):
        result = self.calculator.calculate("-3", "4", "5")

        self.assertEqual(
            result,
            (None, "Стороны должны быть положительными")
        )


if __name__ == "__main__":
    unittest.main()
