# Задача 16.
# Требуется вычислить, сколько раз встречается некторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N - количество элементов в массиве, и число, которое необходимо проверить - X.
# 5 -> 12343
# 3 -> 2

import random
n = int(input('Введите длину массива: '))
l =[]
for num in range(0,n):
    random_number = round(random.randint(0,5))
    l.append(random_number)
print(l)

x = int(input('Введите число для проверки повторений в массиве: '))
count = 0
for i in range(0, len(l)):
    if x == l[i]:
        count += 1

print(x, '->', count)
