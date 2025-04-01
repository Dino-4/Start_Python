#___________________________for____________________

for i  in range(2):      # i - название переменной цикла (может быть любым). range(количество повторений)
    a = 'Kondratev Denis'  # <------ блок команд, который выполняется в цикле for, называется телом цикла.
    print(a)
# ^ В блок команд входят все строки, расположенные с отступом от строки с инструкцией for,
# | вплоть до следующей строки без отступа.
print('\n\n')

for i in range(5):
    num = int(input())
    print("Квадрат вашего числа равен:", num * num)

print("Цикл завершен")  # < ---- не содержит отступа, поэтому не является частью цикла и будет выполнена всего один раз,
# после того как цикл завершится.
print('\n\n')

# ___________________Варианты исполнения кода_______________
# 1
print("A")
print("B")

for i in range(5):
    print("C")              #  < -------- только эта часть будет выполняться заданное количество раз
    print("D")

print("E")
print('\n\n')


#__________________________________________________
# 2
print('A')
print('B')

for i in range(5):
    print('C')           # < -------- в программе может быть сколько угодно циклов

for i in range(5):
    print('D')           # < -------- в программе может быть сколько угодно циклов

print('E')
print('\n\n\n')
#______________________________________________________



#_____________________Переменная цикла____________________________

for i in range(10):     # < ----- Python устанавливает значение переменной цикла i = 0.
    print(i)            # Каждый раз, когда мы повторяем тело цикла, Python увеличивает значение переменной на 1.
print('\n\n')

            # -------- > в Python цикл for начинается с 0 < -----------


for i in range(10):
    print(i, '- Привет')      # < -------- можно использовать для отслеживания номера итерации

# Если мы хотим начать с 1, то можем написать код:

for i in range(10):
    print(i + 1, '-- Привет')  # за счет выражения i + 1, мы начинаем вывод с 1, а не с 0.

print('\n\n\n')





     # ---------- > Для переменных цикла обычно используют буквы i, j, k.  < -------------
     #  Если переменная цикла не используется в теле цикла, то указывайте вместо неё символ нижнего подчеркивания _.









#__________________Функция range() параметром (ами)____________________

for i in range(1, 5):   # < --------- правое число(правая граница) не учитывается
    print(i)   # < ---------- результат последовательность чисел 1234

for i in range(1, 6):
    print(i)    # < ---------- результат последовательность чисел 12345
print('\n\n\n')


for i in range(1, 1000):     # < ------ программа выводит те числа из промежутка [1;999], которые оканчиваются на 7.
    if i % 10 == 7:
        print(i)
print('\n\n\n')


# шаг в последовательности функции range() равна 1, для того что бы поменять шаг последовательности
# задается третий параметр

                   # range(страт, стоп, шаг)
                   # range(start, stop, step)
for i in range(1, 100, 3):   # < ----- шаг последовательности равен 3
    print(i)


for i in range(56, 171, 2):     # < ---------------- Более эффективный код
    print(i)
# ДВА ЭДЕНТИЧНЫХ КОДА ПО СВОЕЙ СУТИ
for i in range(56, 171, 2):     # < ------------------ Менее эффективный код
    if i % 2 == 0:
        print(i)
print('\n\n\n')


#___________________________Отрицательный шаг генерации______________________
                      # |
                       #|
                       #V
for i in range(20, 10, -1):   # если шаг функции отрицательный, то последовательность будет убывать
    print(i)



for i in range(5, 0, -1):
    print(i, end=' ')
print('Взлетаем!')
