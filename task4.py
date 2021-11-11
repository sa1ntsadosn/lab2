print('Введите x:')
x = int(input())
print('Введите g:')
g = int(input())
cos = 1
a1 = 1
a2 = -1
a3 = 2
a4 = 2
x2 = x * x
while (x2 / a3) >= g:
    cos = cos + a2 * x2 / a3
    a1 = a1 + 1
    a4 = a4 + 2
    x2 = x2 * x
    a3 = a3 * (a4 - 1) * a4
    a2 = a2 * (-1)
    print('cos(x)={}'.format(str(cos)))
