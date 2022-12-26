# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь вводит 
# натуральное число N - количество элементов в массиве, и число которое необходимо проверить - X.
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

def findKClosestElements(l, k, target):
 
    left = 0
    right = len(l) - 1
 
    while right - left >= k:
        if abs(l[left] - target) > abs(l[right] - target):
            left = left + 1
        else:
            right = right - 1
 
    return l[left:left + k]

if __name__ == '__main__':
    n = int(input('Введите длину массива: '))
    l =[]
    for num in range(0,n):
        random_number = round(random.randint(0,10))
        l.append(random_number)
    print(l)
    target = int(input('Введите число для поиска ближайшего: '))
    k = 1
 
print(findKClosestElements(l, k, target))