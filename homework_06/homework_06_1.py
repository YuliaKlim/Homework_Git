value = input('How was your day?\n')
print(value)

unical_symbol_1 = 'a'
unical_symbol_2 = 'D'
unical_symbol_3 = 'h'
unical_symbol_4 = 'M'
unical_symbol_5 = 'r'
if value.count(unical_symbol_1) > 10:
    print(f'The number of "a" symbols is greater than 10: True')
else:
    print(f'The number of "a" symbols is greater than 10: False')
if value.count(unical_symbol_2) > 10:
    print(f'The number of "D" symbols is greater than 10: True')
else:
    print(f'The number of "D" symbols is greater than 10: False')
if value.count(unical_symbol_3) > 10:
    print(f'The number of "h" symbols is greater than 10: True')
else:
    print(f'The number of "h" symbols is greater than 10: False')
if value.count(unical_symbol_4) > 10:
    print(f'The number of "M" symbols is greater than 10: True')
else:
    print(f'The number of "M" symbols is greater than 10: False')
if value.count(unical_symbol_5) > 10:
    print(f'The number of "r" symbols is greater than 10: True')
else:
    print(f'The number of "r" symbols is greater than 10: False')