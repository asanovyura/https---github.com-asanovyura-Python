# Задача №34 
song_list = "пара-ра-рам рам-пам-папам па-ра-па-па".split()
test_list = "яиюэоаыуеё"
result = set()

for i in song_list:
    result.add(sum(list(map(lambda x: sum(1 for letter in x if letter in test_list), i))))
    
print('Парам пам-пам' if len(result) == 1 else 'Пам парам') 