#____________ЦЕЛЫЕ ЧИСЛА____________

num1 = 7  # Числа обозначаются без кавычек (в отличии от текста)
num2 = 10
num3= ((num1+num2)*2)/2  # Основные операции с числами

print(num3)
print('\n\n\n')

a=8
b=4

print(a + b)
print(a - b)   # <-----------Основные операции с числами
print(a * b)
print(a / b)
print('\n\n\n')

#____________Порядок выполнения операций

num1 = 2 + 3 * 4
num2 = (2 + 3) * 4   # Последовательность вычислений точно такая же как и в математике !

print(num1, num2, sep=' ||| ')
print('\n\n\n')

#________________Преобразование типов_______________

s = ('1997')
year = int(s)         # для преобразования строки к целому числу используется команда int()
print('Я родился в', year, end='!!!')
print('\n\n\n')


# num1 = int(input())
#num2 = int(input())     #<------------ Для подсчета одного целого числа пишется такой код

#print(num1 + num2)
print('\n\n\n')

#____________________Преобразование целого числа к строке___________________

num = 17
s = str(num)
# num2 = input()
#print(s + num2)
# Для преобразования целого числа в строку, мы используем команду str()


# Сокращение int происходит от английского integer – целый. <---------- !!!!!!

# num1 = -6      # унарный минус     <------------ !!!!!!!!!!!!!!!!
# num2 = 17 - 7  # бинарный минус

