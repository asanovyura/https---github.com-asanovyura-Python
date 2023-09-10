# Задача №34 
# song_list = "пара-ра-рам рам-пам-папам па-ра-па-па".split()
# test_list = "яиюэоаыуеё"
# result = set()

# for i in song_list:
#     result.add(sum(list(map(lambda x: sum(1 for letter in x if letter in test_list), i))))
    
# print("Парам пам-пам" if len(result) == 1 else "Пам парам") 

# Задача №36 
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = [str(operation(i, j)) for j in range(1, num_columns + 1)]
        print(" ".join(row))
print_operation_table(lambda x, y: x * y)