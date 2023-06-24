"""
Defines the geometric drawing objects, such as points and lines.
"""
from __future__ import annotations

import math
from typing import NamedTuple

Number = int | float


class Point(NamedTuple):
    """
    A coordinate in 2-dimensional space.
    """
    x: Number
    y: Number

    def __eq__(self, other: Point) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __add__(self, other: Number | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, Number):
            return Point(self.x + other, self.y + other)
        else:
            return NotImplemented

    def __radd__(self, other: Number | Point) -> Point:
        return self.__add__(other)

    def __sub__(self, other: Number | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, Number):
            return Point(self.x - other, self.y - other)
        else:
            return NotImplemented

    def __rsub__(self, other: Number | Point) -> Point:
        return self.__sub__(other)

    def __mul__(self, other: Number | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, Number):
            return Point(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other: Number | Point) -> Point:
        return self.__mul__(other)

    def __imul__(self, other: Number | Point) -> Point:
        return self.__mul__(other)

    def rotate(self, angle: Number) -> Point:
        """
        Rotate the point anticlockwise by an angle.

        :param angle: The angle to rotate by, in radians.

        :return: A new rotated point.
        """
        return Point(
            round(self.x * math.cos(angle) - self.y * math.sin(angle), 8),
            round(self.x * math.sin(angle) + self.y * math.cos(angle), 8),
        )


class Line:
    """
    A line between two points.
    """
    start: Number | Point
    end: Number | Point

    def __init__(self, start: Number | Point, end: Number | Point):
        self.start = start if isinstance(start, Point) else Point(start, start)
        self.end = end if isinstance(end, Point) else Point(end, end)

    def __str__(self):
        return f"Line({self.start}, {self.end})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: Line) -> bool:
        if isinstance(other, Line):
            return self.start == other.start and self.end == other.end
        else:
            return NotImplemented

    def __add__(self, other: Number | Point) -> Line:
        if isinstance(other, Line):
            raise TypeError("Cannot add two lines together.")
        elif isinstance(other, (Number, Point)):
            return Line(self.start + other, self.end + other)
        else:
            return NotImplemented

    def __radd__(self, other: Number | Point) -> Line:
        return self.__add__(other)

    def rotate(self, angle: Number) -> Line:
        """
        Rotate the line anticlockwise by an angle about its starting
        point.

        :param angle: The angle to rotate by, in radians.

        :return: A new rotated line.
        """
        return Line(self.start, self.start + (self.end - self.start).rotate(angle))
