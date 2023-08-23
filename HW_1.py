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

"""Задача № 12"""
sum = int(input('Задай сумму двух чисел: '))
mult = int(input('Задай произведение чисел: '))

for x in range(sum):
    for y in range(mult):
        if sum == x + y and mult == x * y:
            print(f'\n Первое число = {x} \n Второе число = {y}')
