
import unittest
from unittest.mock import Mock, patch

from src.calculator import TriangleCalculator
from src.database import Database
from src.user_interface import UserInterface
from src.external_service import ExternalService
from src.controller import Controller


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.calculator = TriangleCalculator()
        self.database = Database(":memory:")
        self.user_interface = Mock(spec=UserInterface)
        self.external_service = Mock(spec=ExternalService)

        self.controller = Controller(
            self.calculator,
            self.database,
            self.user_interface,
            self.external_service
        )

    def tearDown(self):
        self.database.close()

    def test_new_triangle(self):
        self.user_interface.get_data.return_value = ("3", "4", "5")

        result = self.controller.run()

        self.assertEqual(
            result,
            "Тип треугольника: разносторонний"
        )

        self.assertEqual(
            self.database.get_record(3, 4, 5),
            ("разносторонний", None)
        )

        self.external_service.send_result.assert_called_once_with(
            result
        )

    def test_existing_triangle(self):
        self.user_interface.get_data.return_value = ("5", "5", "5")

        with patch.object(
            self.calculator,
            "calculate",
            wraps=self.calculator.calculate
        ) as mock_calculate:

            self.controller.run()
            self.controller.run()

            mock_calculate.assert_called_once()

        self.assertEqual(
            self.external_service.send_result.call_count,
            2
        )
    def test_invalid_triangle(self):
        self.user_interface.get_data.return_value = ("1", "2", "10")

        result = self.controller.run()

        self.assertIn("Ошибка:", result)

        record = self.database.get_record(1, 2, 10)

        self.assertIsNotNone(record)
        self.assertEqual(
            record[1],
            "Треугольник не существует"
        )

        self.external_service.send_result.assert_called_once_with(
            result
        )


if __name__ == "__main__":
    unittest.main()
