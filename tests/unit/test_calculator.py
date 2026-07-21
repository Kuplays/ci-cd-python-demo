import allure
import pytest

from app.calculator import add, divide, multiply, power, subtract


@allure.feature("Calculator")
@allure.story("Addition")
@allure.title("Add two numbers")
def test_add_two_positive_numbers():
    with allure.step("Calculate 5 + 5"):
        result = add(5, 5)

    with allure.step("Check result is 10"):
        assert result == 10


@allure.feature("Calculator")
@allure.story("Subtraction")
@allure.title("Subtract two numbers")
def test_subtract_two_numbers():
    with allure.step("Calculate 5 - 5"):
        result = subtract(5, 5)

    with allure.step("Check result is 0"):
        assert result == 0


@allure.feature("Calculator")
@allure.story("Multiplication")
@allure.title("Multiply two numbers")
def test_multiply_two_numbers():
    with allure.step("Calculate 5 * 5"):
        result = multiply(5, 5)

    with allure.step("Check result is 25"):
        assert result == 25


@allure.feature("Calculator")
@allure.story("Division")
@allure.title("Divide two numbers")
def test_divide_two_numbers():
    with allure.step("Calculate 5 / 5"):
        result = divide(5, 5)

    with allure.step("Check result is 1.0"):
        assert result == 1.0


@allure.feature("Calculator")
@allure.story("Division")
@allure.title("Divide by zero raise an error")
def test_divide_by_zero_raises_error():
    with allure.step("Try to divide by 0"):
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            divide(5, 0)


@allure.feature("Calculator")
@allure.story("Power")
@allure.title("Raise number to a power")
def test_power():
    with allure.step("Calculate 5^2"):
        result = power(5, 2)

    with allure.step("Check result is 25"):
        assert result == 25
