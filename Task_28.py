# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4

def sm(a, b):
    if b == 0:
        return a
    return sm(a+1, b-1)


A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
print(f'{A} + {B} = {sm(A,B)}')
