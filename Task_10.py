# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Сколько монет лежит на столе: '))
m = list(filter(lambda x: x == 0 or x == 1, [int(x) for x in input(
    'Введите через пробел как лежат монеты, где 1 - это "Герб", а 0 - "Решка": ').split()][:n]))
k = sum(m)
print(
    f'Минимальное количество монет для переворачивания: {[len(m)-k, k][k <= len(m)-k]}')
