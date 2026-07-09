import pytest

from app.calculator import add, divide, multiply, power, subtract


def test_add_two_positive_numbers():
    result = add(2, 3)

    assert result == 5


def test_subtract_two_numbers():
    result = subtract(10, 4)

    assert result == 6


def test_multiply_two_numbers():
    result = multiply(3, 4)

    assert result == 12


def test_divide_two_numbers():
    result = divide(10, 2)

    assert result == 5.0


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(10, 0)


def test_power():
    result = power(2, 3)

    assert result == 8
