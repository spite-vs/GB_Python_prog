# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

S = int(input('Сколько журавликов было сделано: '))
if S % 6 == 0:
    print(
        f'Петя и Серёжа сделали по {S//6} лошпетских журавликов, а терпила Катя {S*4//6}.')
else:
    print('Чёт ты напутал, пересчитай-ка ещё раз журавликов.')
