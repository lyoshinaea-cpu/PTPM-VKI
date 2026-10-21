import logging
import math





def parse_sides(side_a, side_b, side_c):
    try:
        a = float(side_a)
        b = float(side_b)
        c = float(side_c)
        logging.debug(
            f"Преобразование во float выполнено успешно: "
            f"A={a}, B={b}, C={c}"
        )
        return a, b, c
    except ValueError:
        return None





def are_sides_positive(a, b, c):
    return a > 0 and b > 0 and c > 0






def is_triangle(a, b, c):
    return (
        a + b > c
        and a + c > b
        and b + c > a
    )


def get_triangle_type(a, b, c):
    if a == b == c:
        return "равносторонний"
    if a == b or a == c or b == c:
        return "равнобедренный"
    return "разносторонний"






def calculate_coordinates(a, b, c):
    x_c = (a ** 2 + c ** 2 - b ** 2) / (2 * a)
    y_c = math.sqrt(max(c ** 2 - x_c ** 2, 0))
    points = [
        (0.0, 0.0),
        (a, 0.0),
        (x_c, y_c)
    ]
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)
    width = max_x - min_x
    height = max_y - min_y

    if height == 0:
        scale = 100 / width
    else:
        scale_x = 100 /  width
        scale_y = 100 / height
        scale = min(scale_x, scale_y)

    coordinates = []

    for x, y in points:
        new_x = x * scale
        new_y = y * scale
        coordinates.append(
            (
                int(round(new_x)),
                int(round(new_y))
            )
        )
    logging.debug(
        f"Рассчитаны координаты вершин: {coordinates}"
    )
    return coordinates