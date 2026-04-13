def my_sum(number1, number2):
    return number1 + number2

def arithmetic_mean(list) -> float:
    total_sum = sum(list)
    result = total_sum / len(list)
    return result

def my_string(str) -> str:
    result = "".join(reversed(str))
    return result

def find_substring(str1, str2):
    index_str = str1.find(str2)
    return index_str

def list_sum_even(list):
    sum_even = sum(val for val in list if val % 2 == 0)
    return sum_even