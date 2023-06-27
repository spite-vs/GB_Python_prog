# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число n – количество холодильников. В последующих строках вводятся строки,
# содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3

# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

n = int(input('Сколько холодильников проверяем? '))
coldodilnik = []
zaraza = 'anton'
mn = len(zaraza)
mx = 100
for i in range(n):
    coldodilnik.append(input(f'Что там в {i+1} холодильнике написано: '))
    while mn > len(coldodilnik[i]) or len(coldodilnik[i]) > mx:
        coldodilnik[i] = input(
            f'Не, куда-то не туда смотришь, должно быть от {mn} до {mx}, давай ещё раз: ')
napomoiky = []
for x in range(len(coldodilnik)):
    k = 0
    test = ''
    for y in zaraza:
        if i == len(coldodilnik[x])-1:
            break
        for i in range(k, len(coldodilnik[x])):
            if y == coldodilnik[x][i]:
                test += y
                k = i+1
                break
    if test == zaraza:
        napomoiky.append(x+1)
if len(napomoiky) > 0:
    print(f'Придётся выкинуть', ', '.join(
        map(str, napomoiky)), 'холодильники.')
else:
    print('Ну всё чики-пуки должно быть с твоими холодильниками, если ничего не напутал.')
