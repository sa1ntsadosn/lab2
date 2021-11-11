a = int(input("Введите возраст:"))
if a > 100:
    print("Недопустимый возраст")
if a < 1:
    print("Возраст не должен быть меньше 1!")
s1 = a % 10
s2 = a % 100
if (s1 == 1 and s2 != 11):
    print('{} год'.format(str(a)))
elif (2 <= s1 <= 4 and (10 < s2 >= 20)):
    print('{} года'.format(str(a)))
else:
    print('{} лет'.format(str(a)))