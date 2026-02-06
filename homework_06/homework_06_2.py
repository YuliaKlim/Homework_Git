letter_big = 'H'
letter_small = 'h'
while True:
    value = input('Enter a word containing the letter "H" or "h":\n')
    print(value)
    if letter_big in value:
        print('The letter "H" was found in the word')
        break
    elif letter_small in value:
        print('The letter "h" was found in the word')
        break
    else:
        print('The letter "H" or "h" was not found in the word')