# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int
import random

num = random.randint(3, 10)
my_list = list(range(num))
print(my_list)
for i in range(len(my_list) - 1):
    temp_number = my_list[i]
    num = random.randint(i + 1, len(my_list) - 1)
    my_list[i] = my_list[num]
    my_list[num] = temp_number
print(my_list)
