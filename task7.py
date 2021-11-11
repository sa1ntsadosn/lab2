from tabulate import tabulate

a1 = int(input('Введите 1-ое число:'))
a2 = int(input('Введите 2-ое число:'))
a3 = int(input('Введите 3-ое число:'))
if a1 > a2 and a1 > a3:
    max = a1
    print('Произведение 2-х наименьших чисел {}'.format(a2 * a3))
    tabl = [['Таблица умножения на', '2', '3', '4', '5'],
            ['1-ое {}'.format(a2), a2 * 2, a2 * 3, a2 * 4, a2 * 5],
            ['2-ое {}'.format(a3), a3 * 2, a3 * 3, a3 * 4, a3 * 5]]
    print(tabulate(tabl, tablefmt="grid"))
if a2 > a1 and a2 > a3:
    max = a2
    print('Произведение 2-х наименьших чисел {}'.format(a1 * a3))
    tabl = [['Таблица умножения на', '2', '3', '4', '5'],
            ['1-ое {}'.format(a1), a1 * 2, a1 * 3, a1 * 4, a1 * 5],
            ['2-ое {}'.format(a3), a3 * 2, a3 * 3, a3 * 4, a3 * 5]]
    print(tabulate(tabl, tablefmt="grid"))
if a3 > a1 and a3 > a2:
    max = a3
    print('Произведение 2-х наименьших чисел {}'.format(a1 * a2))
    tabl = [['Таблица умножения на', '2', '3', '4', '5'],
            ['1-ое {}'.format(a1), a1 * 2, a1 * 3, a1 * 4, a1 * 5],
            ['2-ое {}'.format(a2), a2 * 2, a2 * 3, a2 * 4, a2 * 5]]
    print(tabulate(tabl, tablefmt="grid"))
