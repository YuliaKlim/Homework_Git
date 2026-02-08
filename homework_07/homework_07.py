# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print('Task 1')
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    max_number = 10
    # Complete the while loop condition.
    while multiplier <= max_number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18
# 3x7=21
# 3x8=24

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("Task 2")

def test_sum(number1, number2) -> int:
    return number1 + number2

print(test_sum(5, 10))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("Task 3")

def arithmetic_mean(list) -> float:
    total_sum = sum(list)
    result = total_sum / len(list)
    print(result)
    return result

my_list = [1, 2, 3, 4, 5]
arithmetic_mean(my_list)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("Task 4")

def my_string(str) -> str:
    result = "".join(reversed(str))
    return result

result_string = my_string("Hello, world!")
print(result_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("Task 5")

def my_list_words(list) -> str:
    longest_word = max(list, key=len)
    return longest_word

print(my_list_words(["Hi", "world", "Python"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("Task 6")

def find_substring(str1, str2):
    index_str = str1.find(str2)
    return index_str

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
print("Task 7")

# Функція list_sum_even(list) сумує парні числа у листі і повертає результат виконання даної опервції
def list_sum_even(list):
    sum_even = sum(val for val in list if val % 2 == 0)
    return sum_even

# Приклад використання
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result_sum = list_sum_even(my_list)
print(result_sum)

# task 8
print("Task 8")

# Функція only_string_from_list(list) відбирає змінні типу string у листі
# і повертає новий лист тільки зі стрінговими змінними
def only_string_from_list(list) -> list:
    list_str = [val for val in list if isinstance(val, str)]
    return list_str

# Приклад використання
random_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
result_random_list = only_string_from_list(random_list)
print(result_random_list)

# task 9
print("Task 9")

# Функція find_symbol(symb) знаходить заданий символ і рахує його кількість.
# Якщо кількість знаходжень перевищує 10, то фукція повертає True, якщо ні - False
def find_symbol(symb) -> bool:
    text = input('Please input symbols:\n')
    # Знаходимо символ, котрий зустрічається більше 10 раз
    if text.count(symb) > 10:
        return True
    else:
        return False

# Приклад використання
symb = 'h'
result = find_symbol(symb)
print(result)

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
print("Task 10")

# Функція first_person_record(list) додає дані по людині на початку списку, що заносяться через консоль
def first_person_record(list) -> list:
    name = input('Please input name:\n')
    surname = input('Please input surname:\n')
    age = int(input('Please input age:\n'))
    profession = input('Please input profession:\n')
    city = input('Please input city:\n')
    list.insert(0, (name.title(), surname.title(), age, profession.title(), city.title()))
    return list

# Приклад використання
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago')]

print(first_person_record(people_records))