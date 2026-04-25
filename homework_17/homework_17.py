print('Task_1.1')
# Create Generator even numbers
def even_num_generator(n):
    current = 0
    while current <= n:
        yield current
        current += 2
# Example of use
for num in even_num_generator(20):
    print(num, end=' ')

print('\nTask_1.2')
# Create Generator Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
# Example of use
for num in fibonacci_generator(100):
    print(num, end=' ')

print('\nTask_2.1')
# Create Iterator reverse list
class MyReverseIterator:
    def __init__(self, items_list):
        self.items_list = items_list
        self.index = len(items_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.items_list[self.index]
        self.index -= 1
        return value
# Example of use
my_rev_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rev_iter = MyReverseIterator(my_rev_list)

for item in rev_iter:
    print(item, end=' ')

print('\nTask_2.2')
# Create Iterator even numbers
class MyEvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        value = self.current
        self.current += 2
        return value
# Example of use
even_num_iter = MyEvenNumbers(30)

for num in even_num_iter:
    print(num, end=' ')

print('\nTask_3.1')
# Create Decorator logging function
def logger_dec(func):
    def wrapper(*args, **kwargs):
        print(f'Function call: {func.__name__}')
        print(f'Arguments: args={args}, kwargs={kwargs}')

        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper
# Example of use
@logger_dec
def square(x):
    return x ** 2

print(square(5))
print(square(8))

print('\nTask_3.2')
# Create Decorator catching and handling exceptions
def exceptions_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'An error was found in the function {func.__name__}: {e}')
            return None
    return wrapper

# Example of use
@exceptions_dec
def division(x, y):
    return int(x / y)

print(division(25, 5))
print(division(1, 0))



