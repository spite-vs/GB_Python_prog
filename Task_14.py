# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число, до которого вы хотите увидеть все степени двойки: '))
if N < 0:
    print('Таких степеней нет')
else:
    k = 0
    print(f'Спепени двойки до {N}:')
    while 2**k <= N:
        print(f'2^{k} = {2**k}')
        k += 1
