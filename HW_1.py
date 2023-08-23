# """"Задача № 10"""
# n = int(input('Введите количество монеток: '))
# count = 0
# for i in range(n):
#     coin = int(input('Введите значение 1 - "орёл" или 0 - "решка": '))
#     count += coin
#     i += 1
# if count <= n//2:
#     print('Минимальное количество монет, которые нужно перевернуть ', count)
# else:
#     print('Минимальное количество монет, которые нужно перевернуть ', n - count)

# """Задача № 12"""
# S = int(input('Задай сумму двух чисел: '))
# P = int(input('Задай произведение чисел: '))

# for x in range(S):
#     for y in range(P):
#         if S == x + y and P == x * y:
#             print(f'\n Первое число = {x} \n Второе число = {y}')

"""Задача № 14"""
number = abs(int(input('\n Введите число: ')))

stop = 0
degree = 2
for i in range(number):
    if stop != 1:
        degree = degree ** i
        if degree <= number:
            print(degree, end=' ')
            degree = 2
        else:
            stop = 1
    else:
        i = number