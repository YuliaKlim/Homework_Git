def sum_array_elements(elements):
    # print(elements)
    sum = 0
    for i in elements:
        try:
            sum += int(i)
        except ValueError as e:
            print(f'Some elements are not numbers')
    return sum

array_sum = ['1,3,5,7', '2,4,6,8', 'abc,0,9']
for x in array_sum:
    print(sum_array_elements(x.split(',')))



