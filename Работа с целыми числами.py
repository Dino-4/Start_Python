#____________________Работа с целыми числами________________________
from email.quoprimime import body_check

# Возведение в степень: **
# Остаток от деления: %                      <---------------!!!!!!
# Целочисленное деление: //


#_____ Возведение в степень______

print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** (-1))
print('\n\n\n')

# Оператор возведения в степень (**) может возводить не только в положительную степень,
# но и в отрицательную.

print(2 ** (-2))
print((-3) ** 3)
print('\n\n\n')


# Оператор возведения в степень (**) является правоассоциативным (значение выражения вычисляется справа налево)
# в соответствии с правилами математики. Таким образом,
# выражение x ** y ** z вычисляется как x ** (y ** z).

print(2 ** 2 ** 3)   # 2 ** (2 ** 3) = 2 ** 8
print('\n\n\n')



#______________Целочисленные деления________________


print(4 / 2)
print(10 / 3)
print(10 / 4)
print(10 / 5)
print(10 / 6)
print(10 / 12)
print('\n')
print(4 // 2)              # Важно!!!!!!
print(10 // 3)                #|
print(10 // 4)                #|
print(10 // 5)                #|
print(10 // 6)                #|
print(10 // 12)               #|
print('\n')                   #|
                              #|
print(10 // 3)                #V
print(-10 // 3)
# Округление всегда берётся в меньшую сторону. (Для наглядности запусти код)
print('\n\n\n')

#________________Деление с остатком_______________

# Оператор деления с остатком (%) возвращает остаток от деления двух целых чисел.

print(10 % 3)
print(10 % 4)
print(10 % 5)
print(10 % 6)
print(10 % 12)
print(10 % 20)





# _______________Запомни !!!!_______________
1132
a = -7  # Унарный минус
b = 10 - 3  # Бинарный минус, результат: 7
print('\n\n\n')

# _____Операторы расположены по убываю приоритета. (Приоритетность в выражении)
# ()	Скобки
# **	Возведение в степень
# - (унарный минус)	Унарный минус
# *, /, //, %	Умножение, деление, целочисленное деление, остаток от деления
# +, -	Сложение, вычитание






#______Обработка цифр числа______

# При помощи операции нахождения остатка и целочисленного деления можно достаточно несложно вычислить любую цифру числа.
# Пример:
num = 17
a = num % 10
b = num // 10
print(a)
print(b)
print('\n')
# ЗАПОМНИ! последняя цифра числа определяется всегда как остаток от деления числа на 10 (% 10).
# Чтобы отщепить последнюю цифру от числа, необходимо разделить его нацело на 10 (// 10).

num = 754
a = num % 10
b = (num % 100) // 10
c = num // 100
print(a) # 4
print(b) # 5
print(c) # 7
print('\n\n\n')


#________АЛГОРИТМ ПОЛУЧЕНИЯ ЦИФР СКЛОЛЬКИ УГОДНО ЗНАЧНОГО ЧИСЛА______-

# Последняя цифра: (num % 101) // 100;
# Предпоследняя цифра: (num % 102) // 101;
# Предпредпоследняя цифра: (num % 103) // 102;
# .....
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.

# Программа определяющая число десятков и едениц в двузначном числе:
num = int(input())

last_digit = num % 10
first_digit = num // 10

print('Число десятков = ', first_digit, '\n', 'Число единиц = ', last_digit, sep='')
# Другие вареации
print('Сумма цифр =', last_digit + first_digit) # Сумма цифр двузначного числа
print('Искомое число =', last_digit * 10 + first_digit) # Перестановка цифр двузначного числа

# Вводится трехзначное число и которая выводит на экран его цифры (через запятую).
num1 = int(input())
digit3 = num1 % 10
digit2 = (num1 // 10) % 10
digit1 = num1 // 100

print(digit1, digit2, digit3, sep=',')
