# from math import pow, sqrt
from math import floor

# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())

# num = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#num = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
# pow(num, power): возведение числа num в степень power     <--------!!!!!!!!!
# print(num)








# from math import pi, pow

# R = float(input())

# S = pi * pow(R, 2)
# C = 2 * pi * R

# print(S)
# print(C)



# from math import pow, sqrt

# a = float(input())
# b = float(input())

# print((a + b) / 2)
# print(sqrt(a*b))
# print((2 * a * b) / (a + b))
# print(sqrt((pow(a, 2) + pow(b, 2)) / 2))




# from math import sin, cos, tan, pow, radians

# x = float(input())
# xr = radians(x)

# print(sin(xr) + cos(xr) + pow(tan(xr), 2))





# from math import floor, ceil

# x = float(input())

# xf = floor(x)
# xc = ceil(x)

# print(xf + xc)





# from math import pow, sqrt

# a = float(input())
# b = float(input())
# c = float(input())

# D = pow(b, 2) - 4 * a * c

# if D < 0:
    # print('Нет корней')
# elif D == 0:
   # print(- (b/(2*a)))
# elif D > 0:
   # x1 = ((- b) - sqrt(D)) / (2 * a)
   # x2 = ((- b) + sqrt(D)) / (2 * a)
   # xma = max(x1, x2)
   # xmi = min(x1, x2)
   # print(xmi, xma, sep='\n')




from math import pow, pi, tan

n = float(input())
a = float(input())

S = (n * pow(a, 2)) / (4 * tan(pi / n))

print(S)




