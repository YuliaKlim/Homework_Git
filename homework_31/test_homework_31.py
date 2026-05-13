import allure
import pytest

def my_sum(number1, number2):
    return number1 + number2

def arithmetic_mean(numbers_list) -> float:
    total_sum = sum(numbers_list)
    result = total_sum / len(numbers_list)
    return result

def my_string(input_str) -> str:
    result = ''.join(reversed(input_str))
    return result

@allure.feature(f'Adding')
def test_my_sum():
    with allure.step(f'Calling my_sum with args 12 and 31'):
        result = my_sum(12, 31)
    assert result == 43, f'Expected result: 43, Actual result: {result}'

@allure.feature(f'Arithmetic mean of list')
@pytest.mark.parametrize('input_data, expected_output', [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5)])
def test_arithmetic_mean(input_data, expected_output):
    with allure.step(f'Calling arithmetic_mean with {input_data}'):
        result = arithmetic_mean(input_data)
    assert result == expected_output, f'Expected {expected_output}, got {result}'

@allure.feature('Reverse string')
@pytest.mark.parametrize('input_data, expected_output', [('hello world', 'dlrow olleh')])
def test_reverse_string(input_data, expected_output):
    with allure.step(f'Calling my_string with {input_data}'):
        result = my_string(input_data)
    assert result == expected_output, f'Expected {expected_output}, got {result}'

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--alluredir=allure-report", __file__])
