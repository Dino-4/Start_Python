#__________________ Вложенный оператор _________________

grade = int(input('Введите вашу отмету по 100 бальной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)
print('\n\n')


#_______________________Каскадный условный оператор__________________

# Каскадный условны оператор  if - elif - else

# Следующий код аналогичен по своей сути предыдущему, но написан с применением КАСКАДНОГО УСЛОВНОГО ОПЕРАТОРА
grade = int(input('Введите вашу отметку по 100 бальной системе: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:        # <----------- Не обязательно заканчивать оператор этим блоком, можно остановиться на блоге elif
    print(1)

# Заключительный блок else в операторе if-elif-else является необязательным.
# В таком случае если программа не найдет истинный результат она просто ничего не выведет и закончит свое выполнение без ошибок


