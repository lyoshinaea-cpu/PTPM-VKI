import unittest
from unittest.mock import patch, call

from src.user_interface import ConsoleUserInterface


class TestUserInterface(unittest.TestCase):

    @patch("builtins.input", side_effect=["3", "4", "5"])
    def test_get_data(self, mock_input):
        user_interface = ConsoleUserInterface()

        result = user_interface.get_data()

        self.assertEqual(result, ("3", "4", "5"))

        mock_input.assert_has_calls([
            call("Сторона A: "),
            call("Сторона B: "),
            call("Сторона C: ")
        ])

        self.assertEqual(mock_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()
