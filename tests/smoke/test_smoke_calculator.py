import allure

from app.calculator import add, divide, multiply, subtract


@allure.feature("Calculator")
@allure.story("Smoke")
@allure.title("Basic smoke calculator operations")
def test_basic_operations():
    with allure.step("Check addition"):
        assert add(5, 5) == 10

    with allure.step("Check subtraction"):
        assert subtract(5, 5) == 0

    with allure.step("Check multiply"):
        assert multiply(5, 5) == 25

    with allure.step("Check division"):
        assert divide(5, 5) == 1.0
