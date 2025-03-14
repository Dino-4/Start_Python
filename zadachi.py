# Сравнение паролей

# pas1 = input()
# pas2 = input()

# if pas1 == pas2:
  #  print('Пароль принят')
# else:
 #   print('Пароль не принят')


#_______Четное не четное___________

# num = int(input())

# if num % 2 == 0:
   # print('Четное')
# else:
   # print('Нечетное')



#_______Соотношение___________

# n = int(input())

# n4 = n % 10
# n3 = (n // 10) % 10
# n2 = (n // 100) % 10
# n1 = n // 1000

# if n1 + n4 == n2 - n3:
#    print('ДА')
# else:
#    print("НЕТ")



#age = int(input())

#if age < 18:
    #print('Доступ запрещен')
#else:
    #print('Доступ разрешен')


#____________Арифметическая прогрессия
#n1, n2, n3 = int(input()), int(input()), int(input()) # 1 2 3 или 10 5 0

#if n2 - n1 == n3 - n2:
    #print('YES')
#else:
    #print('NO')

# n1, n2 = int(input()), int(input())

#if n1 > n2:
    #print(n2)
# if n1 < n2:
#else:
    #print(n1)


#n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())
#min = n1

#if n2 < min:
   # min = n2
#if n3 < min:
  #  min = n3
#if n4 < min:
 #   min = n4

#print(min)





#age = int(input())

#if age <= 13:
   # print('детсво')
#if 14 <= age <= 24:
  #  print("молодость")
#if 25 <= age <= 59:
 #   print('зрелость')
#if age >= 60:
  #  print('старость')


n1 = int(input())
n2 = int(input())
n3 = int(input())
min = 0
p_n1 = 0
p_n2 = 0
p_n3 = 0

if n1 >  min:
    p_n1 = n1
if n2 > min:
    p_n2 = n2
if n3 > min:
    p_n3 = n3

print(p_n1 + p_n2 + p_n3)



