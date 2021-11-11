f_1 = 1
f_2 = 1
while (f_2 < 10000):
    f_3 = f_1 + f_2
    f_1 = f_2
    f_2 = f_3
    if (f_2 >= 1000):
        f_4 = f_2
        print('Элементов:{}'.format(str(f_4)))
        break