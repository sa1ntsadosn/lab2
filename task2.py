print('Введите кол-во слагаемых:')
count = int(input())
s = 0
for i in range(1, count + 1, 2):
    s = str(4 / i - 4 / (i + 2))
print('Примерное значение P={}'.format(s))
