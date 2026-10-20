import runpy
import unittest
from unittest.mock import patch

from src import main as app


class TestMain(unittest.TestCase):
    def test_setup_logging(self):
        with patch("src.main.os.makedirs") as mock_mkdir, \
             patch("src.main.logging.FileHandler") as mock_file, \
             patch("src.main.logging.basicConfig") as mock_config:

            app.setup_logging()

            mock_mkdir.assert_called_once()
            mock_file.assert_called_once()
            mock_config.assert_called_once()

    def test_main_success(self):
        with patch("src.main.setup_logging"), \
             patch("src.main.Database") as mock_db, \
             patch("src.main.Controller") as mock_controller, \
             patch("builtins.print") as mock_print:

            result = "Тип треугольника: разносторонний"
            mock_controller.return_value.run.return_value = result

            app.main()

            mock_controller.return_value.run.assert_called_once()
            mock_print.assert_called_once_with(
                f"Результат: {result}"
            )
            mock_db.return_value.close.assert_called_once()

    def test_database_error(self):
        with patch("src.main.setup_logging"), \
             patch("src.main.Database",
                   side_effect=RuntimeError("Ошибка БД")), \
             patch("src.main.logging.exception") as mock_error:

            app.main()

            mock_error.assert_called_once()

    def test_controller_error(self):
        with patch("src.main.setup_logging"), \
             patch("src.main.Database") as mock_db, \
             patch("src.main.Controller") as mock_controller, \
             patch("src.main.logging.exception") as mock_error:

            mock_controller.return_value.run.side_effect = (
                RuntimeError("Ошибка контроллера")
            )

            app.main()

            mock_error.assert_called_once()
            mock_db.return_value.close.assert_called_once()

    def test_execution_as_script(self):
        with patch("os.makedirs"), \
             patch("logging.basicConfig"), \
             patch("logging.FileHandler"), \
             patch("src.database.Database") as mock_db, \
             patch("src.controller.Controller") as mock_controller, \
             patch("builtins.print"):

            mock_controller.return_value.run.return_value = "Тест"

            runpy.run_path(app.__file__, run_name="__main__")

            mock_db.return_value.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
