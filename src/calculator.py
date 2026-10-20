
from src.triangle import (
    parse_sides,
    are_sides_positive,
    is_triangle,
    get_triangle_type
)


class TriangleCalculator:
    def calculate(self, side_a, side_b, side_c):

        sides = parse_sides(side_a, side_b, side_c)

        if sides is None:
            return None, "Стороны должны быть числами"

        a, b, c = sides

        if not are_sides_positive(a, b, c):
            return None, "Стороны должны быть положительными"

        if not is_triangle(a, b, c):
            return None, "Треугольник не существует"

        triangle_type = get_triangle_type(a, b, c)

        return triangle_type, None


