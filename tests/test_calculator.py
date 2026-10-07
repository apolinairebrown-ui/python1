import pytest

from python1.calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6
    assert subtract(-3, -3) == 0
    assert subtract(5.5, 2.25) == 3.25


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12
    assert multiply(5, 0) == 0
    assert multiply(2.5, 4) == 10.0


def test_divide():
    assert divide(20, 4) == 5.0
    assert divide(-9, 3) == -3.0
    assert divide(0, 5) == 0.0
    assert divide(1, 3) == pytest.approx(0.3333333)


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)
