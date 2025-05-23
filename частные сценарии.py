#______________________Подсчет количества_____________________

counter = 0         # < ------- для переменной счетчика удобнее использовать counter или сокращенно cnt
for i in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
print('Было введено', counter, 'чисел, больше 10.')
print('\n\n\n')

# Подсчет количества – это очень частый сценарий. Он состоит из двух шагов:

# 1. Создание переменной счетчика, и придание ей первоначального значения: counter = 0;
# 2. Увеличение переменной счетчика на 1: counter = counter + 1.

counter1 = 0
counter2 = 0      # < ------- для переменной счетчика удобнее использовать counter или сокращенно cnt
for i in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1

print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )
print('\n\n\n')

# подсчитать количество чисел из диапазона [1;100], квадрат которых оканчивается на 4.
counter = 0
for i in range(1, 100):
    if i**2 % 10 == 4:
        counter = counter + 1

print(counter)
print('\n\n\n\n\n\n')






#________________________Вычисление суммы и произведения_____________________

total = 0    # <-------------- Для переменной сумматора и мультипликатора удобно использовать имя total
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num

print('Сумма чисел больших 10 равна',  total)
print('\n\n\n')


total = 0
for i in range(1, 101):
    total = total + i

print('Сумма равна', total)
print('\n\n\n')


total = 0       # для умножения total будет начинаться с единицы (1)
for _ in range(10):
    num = int(input())
    total = total + num

average = total / 10     # находим среднее значение
print('Среднее значение равно', average)
# Аналогичным образом вычисляется произведение.
# При вычислении произведения начальное значение переменной мультипликатора мы устанавливаем равным 1,
# в отличие от сумматора, где оно равно 0.
print('\n\n\n\n\n')





#_____________________Обмен значений переменных_______________________
# Допустим
x = 3
y = 5
# для обмена значениями можно ввести временную перем переменную
temp = x # 3
x = y   # 5        < -------- Такой код используется почти во всех языках программирования
y = temp # 3

# в Python есть более простой способ
x, y = y, x
# В результате выполнения такого кода Python поменяет значения переменных x и y местами.




# ____________________ Сигнальные метки ____________________________

# Сигнальная метка (флажок) может использоваться, когда надо,
# чтобы одна часть программы узнала о происходящем в другой части программы.
num = int(input())
flag = True      # < ------- сигнальная метка

for i in range(2, num):   # range(2, 2) выведет [] == [ничего]. Когда start == stop, последовательность не содержит ни одного элемента.
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False      # < ------- сигнальная метка

if num == 1:
    print('Это единица, она не простая и не составная')
elif flag == True:     # < ------- сигнальная метка
    print('Число простое')
else:
    print('Число составное')
print('\n\n\n')



# ________________ Максимум и минимум ________________

largest = 0      # Для переменных, хранящих наибольшее и наименьшее значения, подходят имена largest и smallest соответственно.
for _ in range(10):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest)


smallest = 0     # Для переменных, хранящих наибольшее и наименьшее значения, подходят имена largest и smallest соответственно.
for _ in range(10):
    num = int(input())
    if num < largest:
        largest = num
print('Наименьшее число равно', largest)


# Возможен вариант когда начальное значение переменной сразу принимается первый элемент последовательности

largest = int(input())  # принимаем ПЕРВОЕ ЧИСЛО В ПОСЛЕДОВАТЕЛЬНОСТИ за максимальное
for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)
print('\n\n\n\n')



# __________________________ Расширенные операторы присваивания ___________________

total = total + num
# РАВЕН
total += num   # < ---------- Расширенный оператор присваивания


counter = counter + 1
# АНАЛОГ
counter += 1

# Расширенный операторы:
# += прибавление
# -= вычитание
# *= умножение
# /= деление
# //= деление на цело
# %= остаток от деления

# _______________________ Примечание ______________________

# Задача:
# На вход подается количество чисел n, затем n чисел.
# Нужно найти два самых больших числа из них.

n = int(input())
total = 0
total2 = 0
for i in range(1, n + 1):
    num = int(input())
    if num > total:
        total2 = total                 #< ----------- думай головой
        total = num
    elif num > total2:
        total2 = num


print(total, total2, sep='\n')
print('\n\n\n')



# Напишите программу, которая считывает последовательность из
# 10 целых чисел и определяет, является ли каждое из них чётным или нет

flag = True
for _ in range(10):
    n = int(input())

    if n % 2 == 1:
        flag = False           # < ------------- Задача с флагами!!!!!!!!


if flag:
    print('YES')
else:
    print('NO')



