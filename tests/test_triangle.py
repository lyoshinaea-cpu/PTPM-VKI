import unittest

from src.triangle import (
    parse_sides,
    are_sides_positive,
    is_triangle,
    get_triangle_type,
    calculate_coordinates,
)


class TestTriangle(unittest.TestCase):

    def test_parse_sides_with_valid_numbers(self):
        result = parse_sides("3", "4", "5")
        self.assertEqual(result, (3.0, 4.0, 5.0))

    def test_parse_sides_with_invalid_input(self):
        result = parse_sides("abc", "4", "5")
        self.assertIsNone(result)

    def test_are_sides_positive_with_zero(self):
        result = are_sides_positive(0, 4, 5)
        self.assertFalse(result)

    def test_are_sides_positive_with_negative_value(self):
        result = are_sides_positive(-3, 4, 5)
        self.assertFalse(result)

    def test_is_triangle_with_valid_sides(self):
        result = is_triangle(3, 4, 5)
        self.assertTrue(result)

    def test_is_triangle_with_equal_sum(self):
        result = is_triangle(1, 2, 3)
        self.assertFalse(result)

    def test_get_triangle_type_equilateral(self):
        result = get_triangle_type(5, 5, 5)
        self.assertEqual(result, "равносторонний")

    def test_get_triangle_type_isosceles_ac(self):
        result = get_triangle_type(5, 8, 5)
        self.assertEqual(result, "равнобедренный")

    def test_get_triangle_type_scalene(self):
        result = get_triangle_type(3, 4, 5)
        self.assertEqual(result, "разносторонний")

    def test_calculate_coordinates_right_triangle(self):
        result = calculate_coordinates(3, 4, 5)
        self.assertEqual(result[0], (5, 5))
        self.assertEqual(result[1][1], 5)
        self.assertEqual(result[2][0], result[1][0])
        self.assertEqual(result[2][1], 95)
