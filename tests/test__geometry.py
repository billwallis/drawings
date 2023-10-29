"""
Tests for the ``drawings/geometry.py`` module.
"""
from __future__ import annotations

import math

import pytest

from drawings.geometry import Line, Number, Point

###
# Point Tests
###


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), Point(1, 2), True),
        (Point(1, 2), Point(1.0, 2.0), True),
        (Point(1, 2), Point(1, 3), False),
    ],
)
def test__point__eq(point: Point, other: Point, expected: bool):
    """
    Test the ``Point.__eq__()`` method.
    """
    assert (point == other) is expected


def test__point__eq__not_implemented():
    """
    Test that ``Point.__eq__()`` is ``False``.
    """
    foo: str
    assert (Point(1, 2) == "3") is False


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(4, 5)),
        (Point(1.0, 2.0), 3.0, Point(4.0, 5.0)),
        (Point(1, 2), Point(3, 4), Point(4, 6)),
    ],
)
def test__point__add(point: Point, other: Number | Point, expected: Point):
    """
    Test the ``Point.__add__()`` and ``Point.__radd__()`` methods.
    """
    assert point + other == expected
    assert other + point == expected


def test__point__add__not_implemented():
    """
    Test that ``Point.__add__()`` fails.
    """
    with pytest.raises(TypeError):
        Point(1, 2) + "3"


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Point(4, 5)),
        ([Point(1, 2), Point(3, 4)], Point(4, 6)),
    ],
)
def test__point__iadd(points: list[Number | Point], expected: Point):
    """
    Test the ``Point.__iadd__()`` method.
    """
    actual = Point(0, 0)
    for point in points:
        actual += point

    assert actual == expected


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(4, 5), 3, Point(1, 2)),
        (Point(4.0, 5.0), 3.0, Point(1.0, 2.0)),
        (Point(4, 6), Point(3, 4), Point(1, 2)),
    ],
)
def test__point__sub(point: Point, other: Number | Point, expected: Point):
    """
    Test the ``Point.__sub__()`` and ``Point.__rsub__()`` method.
    """
    assert point - other == expected


@pytest.mark.parametrize(
    "other, point, expected",
    [
        (3, Point(4, 5), Point(-1, -2)),
        (3.0, Point(4.0, 5.0), Point(-1.0, -2.0)),
    ],
)
def test__point__rsub(other: Number, point: Point, expected: Point):
    """
    Test the ``Point.__sub__()`` and ``Point.__rsub__()`` method.
    """
    assert other - point == expected


def test__point__sub__not_implemented():
    """
    Test that ``Point.__sub__()`` fails.
    """
    with pytest.raises(TypeError):
        Point(1, 2) - "3"


def test__point__rsub__not_implemented():
    """
    Test that ``Point.__rsub__()`` fails.
    """
    with pytest.raises(TypeError):
        "3" - Point(1, 2)


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(4, 5), 3], Point(-7, -8)),
        ([Point(4, 6), Point(3, 4)], Point(-7, -10)),
    ],
)
def test__point__isub(points: list[Number | Point], expected: Point):
    """
    Test the ``Point.__isub__()`` method.
    """
    actual = Point(0, 0)
    for point in points:
        actual -= point

    assert actual == expected


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(3, 6)),
        (Point(1.0, 2.0), 3.0, Point(3.0, 6.0)),
        (Point(1, 2), Point(3, 4), Point(3, 8)),
    ],
)
def test__point__mul(point: Point, other: Number | Point, expected: Point):
    """
    Test the ``Point.__mul__()`` and ``Point.__rmul__()`` method.
    """
    assert point * other == expected
    assert other * point == expected


def test__point__mul__not_implemented():
    """
    Test that ``Point.__mul__()`` fails.
    """
    with pytest.raises(TypeError):
        Point(1, 2) * "3"


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Point(3, 6)),
        ([Point(1, 2), Point(3, 4)], Point(3, 8)),
    ],
)
def test__point__imul(points: list[Number | Point], expected: Point):
    """
    Test the ``Point.__imul__()`` method.
    """
    actual = Point(1, 1)
    for point in points:
        actual *= point

    assert actual == expected


@pytest.mark.parametrize(
    "point, angle, expected",
    [
        (Point(1, 2), math.radians(0), Point(1, 2)),
        (Point(1, 2), math.radians(90), Point(-2, 1)),
        (Point(1, 2), math.radians(180), Point(-1, -2)),
        (Point(1, 2), math.radians(270), Point(2, -1)),
        (Point(1, 2), math.radians(360), Point(1, 2)),
    ],
)
def test__point__rotate(point: Point, angle: Number, expected: Point):
    """
    Test the ``Point.rotate()`` method.
    """
    assert point.rotate(angle) == expected


###
# Line Tests
###


@pytest.mark.parametrize(
    "line, start, end",
    [
        (Line(1, 2), 1, 2),
        (Line(1.0, 2.0), 1.0, 2.0),
    ],
)
def test__line__init__numbers(line: Line, start: Number, end: Number):
    """
    Test the ``Line.__init__()`` method with numbers.
    """
    assert line.start == Point(start, start)
    assert line.end == Point(end, end)


def test__line__init__points():
    """
    Test the ``Line.__init__()`` method with points.
    """
    line = Line(Point(1, 2), Point(3, 4))

    assert line.start == Point(1, 2)
    assert line.end == Point(3, 4)


def test__line__init__mixed():
    """
    Test the ``Line.__init__()`` method with mixed types.
    """
    line = Line(1, Point(3, 4))

    assert line.start == Point(1, 1)
    assert line.end == Point(3, 4)


def test__line__str():
    """
    Test the ``Line.__str__()`` method.
    """
    line = Line(1, Point(3, 4))

    assert str(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"


def test__line__repr():
    """
    Test the ``Line.__repr__()`` method.
    """
    line = Line(1, Point(3, 4))

    assert repr(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"
    assert eval(repr(line)) == line


def test__line__eq__not_implemented():
    """
    Test that ``Line.__eq__()`` is ``False``.
    """
    assert (Line(1, 2) == "3") is False


@pytest.mark.parametrize(
    "line, other, expected",
    [
        (Line(1, 2), 3, Line(4, 5)),
        (Line(1, 2), Point(3, 4), Line(Point(4, 5), Point(5, 6))),
    ],
)
def test__line__add(line: Line, other: Number | Point, expected: Line):
    """
    Test the ``Line.__add__()`` and ``Line.__radd__()`` method.
    """
    assert line + other == expected
    assert other + line == expected


@pytest.mark.parametrize(
    "line, other",
    [
        (Line(1, 2), "3"),
        (Line(1, 2), Line(3, 4)),
    ],
)
def test__line__add__not_implemented(line: Line, other: str | Line):
    """
    Test that ``Line.__add__()`` fails.
    """
    with pytest.raises(TypeError):
        line + other


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Line(Point(4, 5), Point(4, 5))),
        ([Point(1, 2), Point(3, 4)], Line(Point(4, 6), Point(4, 6))),
    ],
)
def test__line__iadd(points: list[Number | Point], expected: Line):
    """
    Test the ``Line.__iadd__()`` method.
    """
    actual = Line(0, 0)
    for point in points:
        actual += point

    assert actual == expected


@pytest.mark.parametrize(
    "line, angle, expected",
    [
        (Line(1, 2), math.radians(0), Line(1, 2)),
        (Line(1, 2), math.radians(90), Line(1, Point(0, 2))),
        (Line(1, 2), math.radians(180), Line(1, Point(0, 0))),
        (Line(1, 2), math.radians(270), Line(1, Point(2, 0))),
        (Line(1, 2), math.radians(360), Line(1, 2)),
    ],
)
def test__line__rotate(line: Line, angle: Number, expected: Line):
    """
    Test the ``Line.rotate()`` method.
    """
    assert line.rotate(angle) == expected
