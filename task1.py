import math

print('Дано уравнение ax^2+bx+c=0')
print('Введите число a:')
a = float(input())
print('Введите число b:')
b = float(input())
print('Введите число c:')
c = float(input())
if a == 0:
    x = -c / b
    print('Ответ: x={}'.format(x))
elif b == 0:
    print('Решений нет.')
elif c == 0:
    x_1 = 0
    x_2 = -b / a
    print('Ответ: x1={}, x2={}'.format(x_1, x_2))
else:
    d = b * b - 4 * a * c
    x_1 = (-b - math.sqrt(d)) / 2 * a
    x_2 = (-b + math.sqrt(d)) / 2 * a
    print('Ответ: x1={}, x2={}'.format(x_1, x_2))
