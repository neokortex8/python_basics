"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

pos_int = int(input("Ведите целое положительное число: "))
max_int=0

while pos_int>0:
    some_int=pos_int%10
    if some_int>=max_int:
        max_int=some_int
    pos_int=pos_int//10
print(max_int)