# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n, m = (int(x)
        for x in input('Введите через пробел размер шоколадки: ').split())
k = int(input('Сколько хотите отломить за раз: '))
if k > n*m:
    print('А морда у тебя не треснет?')
elif k % n == 0 or k % m == 0:
    print('Ломай!')
else:
    print('Пора снова в младших классах подучиться...')