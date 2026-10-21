import logging
import os
import sys
from triangle import (
    parse_sides,
    are_sides_positive,
    is_triangle,
    get_triangle_type,
    calculate_coordinates
)




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
    while True:
        try:
            side_a = input("Введите сторону A: ")
            side_b = input("Введите сторону B: ")
            side_c = input("Введите сторону C: ")
            logging.info(
                f"Получен запрос: A={side_a}, B={side_b}, C={side_c}"
            )
            sides = parse_sides(side_a, side_b, side_c)

            if sides is None:
                triangle_type = ""
                coordinates = [
                    (-2, -2),
                    (-2, -2),
                    (-2, -2)
                ]
                logging.error(
                    f"Неуспешный запрос: A={side_a}, B={side_b}, C={side_c}. "
                    f"Ошибка: введены нечисловые данные. "
                    f"Результат: тип='{triangle_type}', координаты={coordinates}"
                )
                print(f"Тип треугольника: {triangle_type}")
                print(f"Координаты вершин: {coordinates}")
                continue
            a, b, c = sides

            if not are_sides_positive(a, b, c):
                triangle_type = "не треугольник"
                coordinates = [
                    (-1, -1),
                    (-1, -1),
                    (-1, -1)
                ]
                logging.error(
                    f"Неуспешный запрос: A={a}, B={b}, C={c}. "
                    f"Ошибка: стороны должны быть положительными. "
                    f"Результат: тип='{triangle_type}', координаты={coordinates}"
                )
                print(f"Тип треугольника: {triangle_type}")
                print(f"Координаты вершин: {coordinates}")
                continue

            if not is_triangle(a, b, c):
                triangle_type = "не треугольник"
                coordinates = [
                    (-1, -1),
                    (-1, -1),
                    (-1, -1)
                ]
                logging.error(
                    f"Неуспешный запрос: A={a}, B={b}, C={c}. "
                    f"Ошибка: стороны не образуют треугольник. "
                    f"Результат: тип='{triangle_type}', координаты={coordinates}"
                )
                print(f"Тип треугольника: {triangle_type}")
                print(f"Координаты вершин: {coordinates}")
                continue
            triangle_type = get_triangle_type(a, b, c)
            coordinates = calculate_coordinates(a, b, c)
            logging.info(
                f"Успешный запрос: A={a}, B={b}, C={c}. "
                f"Результат: тип='{triangle_type}', координаты={coordinates}"
            )

            print(f"Тип треугольника: {triangle_type}")
            print(f"Координаты вершин: {coordinates}")

        except Exception:
            logging.exception(
                "Произошла непредвиденная ошибка при выполнении программы"
            )






if __name__ == "__main__":
    main()