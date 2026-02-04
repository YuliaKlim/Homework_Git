adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print('task_01')
new_adwentures_of_tom_sawer_01 = adwentures_of_tom_sawer.replace("\n", " ")
print("original text_01:", adwentures_of_tom_sawer)
print("new_text_01:", new_adwentures_of_tom_sawer_01)

# task 02 ==
""" Замініть .... на пробіл
"""
print('task_02')
new_adwentures_of_tom_sawer_02 = new_adwentures_of_tom_sawer_01.replace("....", " ")
print("original text_02:", new_adwentures_of_tom_sawer_01)
print("new_text_02:", new_adwentures_of_tom_sawer_02)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('task_03')
new_adwentures_of_tom_sawer_03 = ' '.join(new_adwentures_of_tom_sawer_02.split())
print("original text_03:", new_adwentures_of_tom_sawer_02)
print("new_text_03:", new_adwentures_of_tom_sawer_03)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('task_04')
new_adwentures_of_tom_sawer_04 = new_adwentures_of_tom_sawer_03.count('h')
print("Count_of_'h':", new_adwentures_of_tom_sawer_04)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('task_05')
big_letters_count = sum(1 for big_letter in new_adwentures_of_tom_sawer_03 if big_letter.isupper())
print(big_letters_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print('task_06')
first_pozition = new_adwentures_of_tom_sawer_03.find('Tom')
second_pozition = new_adwentures_of_tom_sawer_03.find('Tom', first_pozition + 1)
print(second_pozition)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print('task_07')
sentences = new_adwentures_of_tom_sawer_03.split('. ')
adwentures_of_tom_sawer_sentences = '.\n'.join(sentences)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print('task_08')
sentence_4 = sentences[3:4]
print(''.join(sentence_4).lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print('task_09')
for sentence in sentences:
    if sentence.startswith('By the time'):
        print('Find_string_By_the_time')
    else:
        print('Not_found_string_By_the_time')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print('task_10')
sentence_end = sentences[-1:]
words =''.join(sentence_end)
words_count = len(words.split())
print(words_count)
