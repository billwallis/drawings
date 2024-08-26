"""
Draw some shadizzle.
"""

import math

import geometry
import matplotlib.pyplot as plt

Polygon = list[geometry.Line]
Drawing = list[geometry.Line]

THRESHOLD = 0.01
LINE_WIDTH = 1


def _calculate_angle(m: float) -> float:
    """
    Calculate the angle from the positive x-axis of a line with slope ``m``.
    """
    return math.acos(1 / math.sqrt(1 + m**2))


def _calculate_slope(starting_angle: float, rotation: float) -> float:
    """
    Calculate the new slope of a line with starting angle ``starting_angle``
    and rotation ``rotation``.
    """
    return math.tan(starting_angle + rotation)


def _calculate_intersection(
    line_1: geometry.Line,
    line_2: geometry.Line,
) -> geometry.Point:
    """
    Calculate the intersection point of two lines.
    """
    if line_1.slope == line_2.slope:
        raise ValueError("Lines are parallel.")

    if line_1.slope == math.inf:
        x = line_1.start.x
        y = line_2.intercept + line_2.slope * x
        return geometry.Point(x, y)

    if line_2.slope == math.inf:
        x = line_2.start.x
        y = line_1.intercept + line_1.slope * x
        return geometry.Point(x, y)

    x = (line_2.intercept - line_1.intercept) / (line_1.slope - line_2.slope)
    return geometry.Point(x, line_1.intercept + line_1.slope * x)


def _create_polygon(number_of_lines: int) -> Polygon:
    """
    Create a polygon.
    """
    if number_of_lines < 3:  # noqa: PLR2004
        raise ValueError("A polygon must have at least 3 lines.")

    center, radius = geometry.Point(0, 0), geometry.Point(2, 0)
    starting_angle = -3 * math.pi / 2

    points = [
        radius.rotate(
            by=starting_angle + (i * 2 * math.pi / number_of_lines),
            around=center,
        )
        for i in range(number_of_lines)
    ]

    return [geometry.Line(points[i - 1], points[i]) for i in range(len(points))]


def _calculate_spiral(lines: Polygon, angle: float) -> Drawing:
    """
    Calculate the lines of a spiral.
    """
    i, line_1, new_point = 0, lines[0], lines[0].start
    while line_1.length > THRESHOLD and i < 1000:  # noqa: PLR2004
        line_1 = geometry.Line(new_point, line_1.end)
        line_2 = lines[i + 1]

        new_point = _calculate_intersection(line_1.rotate(angle), line_2)
        new_line = geometry.Line(line_1.start, new_point)
        lines.append(new_line)

        i += 1  # just in case the loop doesn't converge
        line_1 = line_2

    return lines


def _draw(lines: Drawing) -> None:
    """
    Draw the lines.
    """
    x_values, y_values = [], []
    for line in lines:
        x_values.extend((line.start.x, line.end.x))
        y_values.extend((line.start.y, line.end.y))

    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.plot(x_values, y_values, linewidth=LINE_WIDTH)
    plt.show()


def main() -> None:
    """
    Draw some shadizzle.
    """
    lines, angle = _create_polygon(4), math.pi / 75
    spiral = _calculate_spiral(lines, angle)
    _draw(spiral)


if __name__ == "__main__":
    main()
