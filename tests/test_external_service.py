import unittest
from unittest.mock import patch

from src.external_service import (
    ExternalService,
    SimulatedExternalService
)


class TestExternalService(unittest.TestCase):

    def test_send_result(self):
        service = SimulatedExternalService()

        with patch("builtins.print") as mock_print:
            service.send_result("Тестовое сообщение")

        mock_print.assert_called_once_with(
            "Имитация отправки на сервер: Тестовое сообщение"
        )

    def test_abstract_interface(self):
        with self.assertRaises(TypeError):
            ExternalService()


if __name__ == "__main__":
    unittest.main()
