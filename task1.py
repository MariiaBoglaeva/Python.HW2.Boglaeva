# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = list(input("Введите вещественное число: "))

if '.' in number:
    number.remove('.')
if ',' in number:
    number.remove(',')
if '-' in number:
    number.remove('-')
sum_digit = 0
for i in number:
    sum_digit += int(i)
print(f"сумма цифр->{sum_digit}")
