#______________________Подсчет количества_____________________

counter = 0
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
counter2 = 0
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
print('\n\n\n')

