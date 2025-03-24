a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif (a == b or a == c or b == c) and (a != b or a != c or b != c):
    print('Равнобедренный')
elif a != b and b != c and c != b:
    print('Разносторонний')

