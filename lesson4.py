'''
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
nArray = []
mArray = []
for i in range(n):
    nArray.append(int(input(f'{i+1}-ый элемент первого множества: ')))
for i in range(m):
    mArray.append(int(input(f'{i+1}-ый элемент второго множества: ')))

identifical = []
for valueN in nArray:
    if valueN in mArray:
        identifical.append(valueN)
distinctValues = [str(ind) for ind in sorted(set(identifical))]
print(f'Числа без повторений: {" ".join(distinctValues)}')
'''

'''
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
n = int(input('Количество кустов:'))
a = [int(ind) for ind in input('Введите через пробел кол-во ягод на каждом кусте: ').split()]
maxCount = 0
for ind in range(len(a)):
    prevInd = ind -1 if ind - 1 >= 0 else len(a) -1
    nextInd = ind +1 if ind +1 < len(a) else 0
    maxCount = max(maxCount, a[prevInd] + a[ind] + a[nextInd])
print(f'Максимальное число ягод, собранных за раз: {maxCount}')
'''

'''
# Задача RLE необязательная. Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
# #апример декодирование
# https://stepik.org/lesson/21300/step/2
# aaabccccCCaB -> 3ab4c2CaB

def encoding(strIn):
    result = []
    oldSymbol = strIn[0]
    count = 1
    for ind in range(1, len(strIn)):
        if oldSymbol == strIn[ind]:
            count = count +1
            continue
        else:
            if count > 1:
                result.append(str(count))
            result.append(oldSymbol)
            count = 1
            oldSymbol = strIn[ind]
    # последний элемент нужно тоже проверить
    if count > 1:
        result.append(str(count))
    result.append(oldSymbol)
    return "".join(result)

def decoding(strIn):
    numbers = [str(ind) for ind in range(10)]
    result = []
    numTmp = ["0"]
    for symbol in strIn:
        if (symbol in numbers):
            numTmp.append(symbol)
        else:
            num = int("".join(numTmp))
            result.append(str(symbol).rjust(num, symbol))
            numTmp = ["0"]
    return "".join(result)

strValue = "aaabccccCCaaaaaaaaaaB"
encodeStr = encoding(strValue)
decodeStr = decoding(encodeStr)
print(f'strValue: {strValue}')
print(f'encodeStr: {encodeStr}')
print(f'decodeStr: {decodeStr}')
'''

# Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:ВсегоИгр Побед Ничьих Поражений ВсегоОчков
#
# Конкретный пример ввода-вывода приведён ниже. Порядок вывода команд произвольный.
# Sample Input: 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
countGame = int(input('Введите количество игр: '))
games = []
for gameNumber in range(countGame):
    games.append(input(f'Данные {gameNumber+1}-ой игры: ').split(';'))
#games = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]
# ключем выступает имя команды, а значением список: на 0 месте - всего игр, на 1 - побед, на 2 - ничьих, на 3 - поражений, на 4 - всего очков
totalTable = {}
for game in games:
    # достаем голы
    goalLeftTeam = int(game[1])
    goalRightTeam = int(game[3])

    dataLeftTeam = [0, 0, 0, 0, 0]
    if (game[0] in totalTable):
        dataLeftTeam = totalTable[game[0]]

    dataRightTeam = [0, 0, 0, 0, 0]
    if (game[2] in totalTable):
        dataRightTeam = totalTable[game[2]]

    # считаем данные по игре
    dataLeftTeam[0] += 1
    dataRightTeam[0] += 1
    if goalLeftTeam > goalRightTeam:
        dataLeftTeam[1] += 1
        dataRightTeam[3] += 1
        dataLeftTeam[4] += 3
    elif goalLeftTeam < goalRightTeam:
        dataRightTeam[1] += 1
        dataLeftTeam[3] += 1
        dataRightTeam[4] += 3
    else:
        dataLeftTeam[2] += 1
        dataRightTeam[2] += 1
        dataLeftTeam[4] += 1
        dataRightTeam[4] += 1

    # обновляем данные по команде в турнирной таблице
    totalTable[game[0]] = dataLeftTeam
    totalTable[game[2]] = dataRightTeam

# размер колонок для красивого вывода
widths = [7, 3, 5, 6, 9, 5]
for team, _ in totalTable.items():
    widths[0] = max(widths[0], len(team))

print('Турнирная таблица:')
print(f'{"Команда".rjust(widths[0], " ")} | Игр | Побед | Ничьих | Поражений | Очков')
for team, data in totalTable.items():
    totalTmp = []
    for ind in range(len(data)):
        totalTmp.append(' | ')
        totalTmp.append(str(data[ind]).rjust(widths[ind +1], " "))
    print(f'{team.rjust(widths[0], " ")}{"".join(totalTmp)}')