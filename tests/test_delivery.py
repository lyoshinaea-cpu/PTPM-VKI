
import unittest

from src.Delivery import calculate_delivery_cost


class TestDelivery(unittest.TestCase):

    def test_delivery_with_valid_data(self):
        result = calculate_delivery_cost(1, 100, "обычный")
        self.assertEqual(result, (700, "2026-09-04"))

    def test_delivery_with_weight_below_minimum(self):
        result = calculate_delivery_cost(0.09, 100, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_delivery_with_zero_distance(self):
        result = calculate_delivery_cost(1, 0, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_delivery_with_invalid_package_type(self):
        result = calculate_delivery_cost(1, 100, "неизвестный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_delivery_with_weight_equal_twenty(self):
        result = calculate_delivery_cost(20.0, 100, "обычный")
        self.assertEqual(result, (1050, "2026-09-04"))

    def test_delivery_with_fragile_package(self):
        result = calculate_delivery_cost(1, 100, "хрупкий")
        self.assertEqual(result, (1000, "2026-09-04"))

    def test_delivery_with_dangerous_package(self):
        result = calculate_delivery_cost(1, 100, "опасный")
        self.assertEqual(result, (1700, "2026-09-04"))

    def test_express_delivery_costs_more(self):
        regular = calculate_delivery_cost(1, 100, "обычный")
        express = calculate_delivery_cost(
            1, 100, "обычный", is_express=True
        )
        self.assertGreater(express[0], regular[0])

    def test_express_delivery_minimum_one_day(self):
        result = calculate_delivery_cost(
            1, 100, "обычный", is_express=True
        )
        self.assertEqual(result[1], "2026-09-04")

    def test_delivery_distance_above_five_hundred(self):
        result = calculate_delivery_cost(1, 501, "обычный")
        self.assertEqual(result[1], "2026-09-05")

    # Новый тест: вес от 5 до 20 кг
    def test_delivery_medium_weight(self):
        result = calculate_delivery_cost(10, 100, "обычный")

        self.assertEqual(result[0], 840)
        self.assertEqual(result[1], "2026-09-04")


if __name__ == "__main__":
    unittest.main()
