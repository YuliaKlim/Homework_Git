list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = [val for val in list1 if isinstance(val, str)]
print(list2)