"""
Tests for the ``drawings/geometry.py`` module.
"""
from __future__ import annotations

import math

import pytest

from drawings.geometry import Line, Point

###
# Point Tests
###

@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(4, 5)),
        (Point(1, 2), Point(3, 4), Point(4, 6)),
    ]
)
def test__point__addition(point: Point, other: float | Point, expected: Point):
    """
    Test the ``Point.__add__()`` and ``Point.__radd__()`` methods.
    """
    assert (point + other) == expected
    assert point.__radd__(other) == expected


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Point(4, 5)),
        ([Point(1, 2), Point(3, 4)], Point(4, 6)),
    ]
)
def test__point__addition_inplace(points: list[float | Point], expected: Point):
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
        (Point(4, 6), Point(3, 4), Point(1, 2)),
    ]
)
def test__point__subtraction(point: Point, other: float | Point, expected: Point):
    """
    Test the ``Point.__sub__()`` and ``Point.__rsub__()`` method.
    """
    assert (point - other) == expected
    assert point.__rsub__(other) == expected


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(4, 5), 3], Point(-7, -8)),
        ([Point(4, 6), Point(3, 4)], Point(-7, -10)),
    ]
)
def test__point__subtraction_inplace(points: list[float | Point], expected: Point):
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
        (Point(1, 2), Point(3, 4), Point(3, 8)),
    ]
)
def test__point__multiplication(point: Point, other: float | Point, expected: Point):
    """
    Test the ``Point.__mul__()`` and ``Point.__rmul__()`` method.
    """
    assert (point * other) == expected
    assert point.__rmul__(other) == expected


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Point(3, 6)),
        ([Point(1, 2), Point(3, 4)], Point(3, 8)),
    ]
)
def test__point__multiplication_inplace(points: list[float | Point], expected: Point):
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
    ]
)
def test__point__rotate(point: Point, angle: float, expected: Point):
    """
    Test the ``Point.rotate()`` method.
    """
    assert point.rotate(angle) == expected


###
# Line Tests
###

def test__line__initialisation__floats():
    """
    Test the ``Line.__init__()`` method with floats.
    """
    line = Line(1, 2)

    assert line.start == Point(1, 1)
    assert line.end == Point(2, 2)


def test__line__initialisation__points():
    """
    Test the ``Line.__init__()`` method with points.
    """
    line = Line(Point(1, 2), Point(3, 4))

    assert line.start == Point(1, 2)
    assert line.end == Point(3, 4)


def test__line__initialisation__mixed():
    """
    Test the ``Line.__init__()`` method with mixed types.
    """
    line = Line(1, Point(3, 4))

    assert line.start == Point(1, 1)
    assert line.end == Point(3, 4)


def test__line__string():
    """
    Test the ``Line.__str__()`` method.
    """
    line = Line(1, Point(3, 4))

    assert str(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"


def test__line__representation():
    """
    Test the ``Line.__repr__()`` method.
    """
    line = Line(1, Point(3, 4))

    assert repr(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"
    assert eval(repr(line)) == line


@pytest.mark.parametrize(
    "line, other, expected",
    [
        (Line(1, 2), 3, Line(4, 5)),
        (Line(1, 2), Point(3, 4), Line(Point(4, 5), Point(5, 6))),
    ]
)
def test__line__addition(line: Line, other: float | Point, expected: Line):
    """
    Test the ``Line.__add__()`` and ``Line.__radd__()`` method.
    """
    assert (line + other) == expected
    assert line.__radd__(other) == expected


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Line(Point(4, 5), Point(4, 5))),
        ([Point(1, 2), Point(3, 4)], Line(Point(4, 6), Point(4, 6))),
    ]
)
def test__line__addition_inplace(points: list[float | Point], expected: Line):
    """
    Test the ``Line.__iadd__()`` method.
    """
    actual = Line(0, 0)
    for point in points:
        actual += point

    assert actual == expected


def test__line__addition_error():
    """
    Test the ``Line.__iadd__()`` method.
    """
    with pytest.raises(TypeError):
        Line(0, 0) + Line(1, 2)


@pytest.mark.parametrize(
    "line, angle, expected",
    [
        (Line(1, 2), math.radians(0), Line(1, 2)),
        (Line(1, 2), math.radians(90), Line(1, Point(0, 2))),
        (Line(1, 2), math.radians(180), Line(1, Point(0, 0))),
        (Line(1, 2), math.radians(270), Line(1, Point(2, 0))),
        (Line(1, 2), math.radians(360), Line(1, 2)),
    ]
)
def test__line__rotate(line: Line, angle: float, expected: Line):
    """
    Test the ``Line.rotate()`` method.
    """
    assert line.rotate(angle) == expected
