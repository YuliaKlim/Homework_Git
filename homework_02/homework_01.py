# task 01 == Виправте синтаксичні помилки
print("task 01:")
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print("task 02:")
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("task 03:")
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print("task 04:")
apples = 2
banana = 4 * apples
print(banana)

# task 05 == виправте назви змінних
print("task 05:")
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("task 06:")
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print("task 07:")
yabluny = 4
grushy = 5 + yabluny
slivy = yabluny - 2
vsiogo_derev = yabluny + grushy + slivy
print(vsiogo_derev)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("task 08:")
t_do_obidu = 5
t_pislya_obidu = t_do_obidu - 10
t_nadvechir = t_pislya_obidu + 4
print(t_nadvechir)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("task 09:")
vsiogo_hlopchiky = 24
vsiogo_divchat = vsiogo_hlopchiky / 2
siogodny_hlopchiky = vsiogo_hlopchiky - 1
siogodny_divchat = vsiogo_divchat - 2
siogodny_ditey = siogodny_hlopchiky + siogodny_divchat
print(siogodny_ditey)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("task 10:")
kniga_1 = 8
kniga_2 = kniga_1 + 2
kniga_3 = (kniga_1 + kniga_2) / 2
vse_knigy = kniga_1 + kniga_2 + kniga_3
print(vse_knigy)