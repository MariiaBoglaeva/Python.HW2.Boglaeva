# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input("Введите число: "))
if number >= 0:
    num_list = list(range(number))
    sum_element = 0
    for i in range(number):
        num_list[i] = round((1 + (i + 1) ** (-1)) ** (i + 1),2)
        sum_element += num_list[i]
    print(f"n={number}-> {num_list}")
    print(f"Сумма {sum_element}")
else:
    print("Введено некорректное число")