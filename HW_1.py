# """"Задача № 22"""
#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# n = int(input("Введите количество элементов 1-го множества: "))
# m = int(input("Введите количество элементов 2-го множества: "))
# first_set = set()
# for i in range(n):
#     x = int(input("Введите элемент 1-го множества: "))
#     first_set.add(x)
# second_set = set()
# for i in range(m):
#     x = int(input("Введите элемент 2-го множества: "))
#     second_set.add(x)
# result = first_set.intersection(second_set)
# result = sorted(list(result))
# print(first_set, ' ', second_set, 'Ответ', result)


# """"Задача № 24"""

N = int(input("Введите колличество кустов: "))
berry_bush = []
for i in range(N):
    a = int(input(f'Введите количество ягод на {i+1} кусте: '))
    berry_bush.append(a)
max_berries = 0
for i in range(N):
    total_berries = berry_bush[i] + berry_bush[(i - 1 + N) % N] + berry_bush[(i + 1) % N]
    if total_berries > max_berries:
        max_berries = total_berries
print("Максимальное число ягод:", max_berries)