
import logging
import os
import sys

from src.calculator import TriangleCalculator
from src.database import Database
from src.user_interface import ConsoleUserInterface
from src.external_service import SimulatedExternalService
from src.controller import Controller


def setup_logging():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir = os.path.join(current_dir, "Logs")
    os.makedirs(logs_dir, exist_ok=True)

    log_file = os.path.join(logs_dir, "file_txt.log")
    log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, encoding="utf-8")
        ]
    )


def main():
    setup_logging()

    logging.info("Логгер успешно сконфигурирован")
    logging.info("Приложение запущено")

    database = None

    try:
        calculator = TriangleCalculator()
        database = Database("triangles.db")
        user_interface = ConsoleUserInterface()
        external_service = SimulatedExternalService()

        logging.info("Все компоненты успешно инициализированы")

        controller = Controller(
            calculator,
            database,
            user_interface,
            external_service
        )

        result = controller.run()

        logging.info(
            f"Запрос успешно обработан. Результат: {result}"
        )

        print(f"Результат: {result}")

    except Exception:
        logging.exception(
            "Произошла непредвиденная ошибка при выполнении программы"
        )

    finally:
        if database is not None:
            database.close()
            logging.info("Соединение с базой данных закрыто")

        logging.info("Работа приложения завершена")


if __name__ == "__main__":
    main()
