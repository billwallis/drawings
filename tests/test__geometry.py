"""
Tests for the ``drawings/geometry.py`` module.
"""
from __future__ import annotations

import math

import pytest

from drawings.geometry import Line, Point


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(4, 5)),
        (Point(1, 2), Point(3, 4), Point(4, 6)),
    ]
)
def test__point__addition(point: Point, other: float | Point, expected: Point):
    """
    Test the ``Point.__add__()`` method.
    """
    assert (point + other) == expected


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(4, 5), 3, Point(1, 2)),
        (Point(4, 6), Point(3, 4), Point(1, 2)),
    ]
)
def test__point__subtraction(point: Point, other: float | Point, expected: Point):
    """
    Test the ``Point.__sub__()`` method.
    """
    assert (point - other) == expected


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(3, 6)),
        (Point(1, 2), Point(3, 4), Point(3, 8)),
    ]
)
def test__point__multiplication(point: Point, other: float | Point, expected: Point):
    """
    Test the ``Point.__mul__()`` method.
    """
    assert (point * other) == expected


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


@pytest.mark.parametrize(
    "line, other, expected",
    [
        (Line(1, 2), 3, Line(4, 5)),
        (Line(1, 2), Point(3, 4), Line(Point(4, 5), Point(5, 6))),
    ]
)
def test__line__addition(line: Line, other: float | Point, expected: Line):
    """
    Test the ``Line.__add__()`` method.
    """
    assert (line + other) == expected


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
