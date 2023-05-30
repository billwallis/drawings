"""
Defines the geometric drawing objects, such as points and lines.
"""
from __future__ import annotations

import math
from typing import Any, NamedTuple


class Point(NamedTuple):
    """
    A coordinate in 2-dimensional space.
    """
    x: float
    y: float

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: float | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return Point(self.x + other, self.y + other)

    def __radd__(self, other: float | Point) -> Point:
        return self.__add__(other)

    def __iadd__(self, other: float | Point) -> Point:
        return self.__add__(other)

    def __sub__(self, other: float | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return Point(self.x - other, self.y - other)

    def __rsub__(self, other: float | Point) -> Point:
        return self.__sub__(other)

    def __isub__(self, other: float | Point) -> Point:
        return self.__sub__(other)

    def __mul__(self, other: float | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other: float | Point) -> Point:
        return self.__mul__(other)

    def __imul__(self, other: float | Point) -> Point:
        return self.__mul__(other)

    def rotate(self, angle: float) -> Point:
        """
        Rotate the point anticlockwise by an angle.

        :param angle: The angle to rotate by, in radians.
        """
        return Point(
            round(self.x * math.cos(angle) - self.y * math.sin(angle), 8),
            round(self.x * math.sin(angle) + self.y * math.cos(angle), 8),
        )


class Line:
    """
    A line between two points.
    """
    def __init__(self, start: float | Point, end: float | Point):
        self.start = start if isinstance(start, Point) else Point(start, start)
        self.end = end if isinstance(end, Point) else Point(end, end)

    def __str__(self):
        return f"Line({self.start}, {self.end})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: Line):
        return self.start == other.start and self.end == other.end

    def __add__(self, other: float | Point) -> Line:
        if isinstance(other, Line):
            raise ArithmeticError("Cannot add two lines together.")
        return Line(self.start + other, self.end + other)

    def __radd__(self, other: Any) -> Line:
        return self.__add__(other)

    def __iadd__(self, other: Any) -> Line:
        return self.__add__(other)

    def rotate(self, angle: float) -> Line:
        """
        Rotate the line anticlockwise by an angle about its starting
        point.

        :param angle: The angle to rotate by, in radians.
        """
        return Line(self.start, self.start + (self.end - self.start).rotate(angle))
