
'''
# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
first = int(input('Введите первый элемент: '))
step = int(input('Введите шаг прогрессии: '))
count = int(input('Введите количество элементов: '))
def delta(n, step):
    return (0 if n -1 < 0 else n -1) * step
for ind in range(count):
    value = first + delta(ind +1, step)
    print(value)
'''

'''
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
#Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#Вывод: [1, 9, 13, 14, 19]

arrayIn = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minIn = int(input('Введите минимум: '))
maxIn = int(input('Введите максимум: '))
result = []
for ind in range(len(arrayIn)):
    if arrayIn[ind] >= minIn and arrayIn[ind] <= maxIn:
        result.append(ind)
print(result)
'''


'''
# Задача HARD SORT необязательная. 
# Считается за три обязательных Задайте двумерный массив из целых чисел. 
# Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз. 
# Например, задан массив: 
# 1 4 7 2
# 5 9 10 3 
# После сортировки 
# 1 2 3 4
# 5 7 9 10
from random import randint

arraySize = [int(v) for v in input('Размер двумерного массива через пробел: ').split()]
arrayRaw = []
for i in range(arraySize[0]):
    arrayRaw.append([randint(1, 20) for _ in range(arraySize[1])])

#arraySize = [2, 4]
#arrayRaw = [[1, 4, 7, 2], [5, 9, 10, 3]]
print(arrayRaw)

size = arraySize[0] * arraySize[1]
for indI in range(size -1):
    rowI = indI // arraySize[1]
    columnI = indI % arraySize[1]
    for indJ in range(indI +1, size):
        rowJ = indJ // arraySize[1]
        columnJ = indJ % arraySize[1]
        if arrayRaw[rowI][columnI] > arrayRaw[rowJ][columnJ]:
            tmp = arrayRaw[rowJ][columnJ]
            arrayRaw[rowJ][columnJ] = arrayRaw[rowI][columnI]
            arrayRaw[rowI][columnI] = tmp
print(arrayRaw)
'''

# Задача 2 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры), 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно 
# и только один раз переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.
from random import randint
from random import choice

# Посчитать максимальное количество цифр значения в двумероном массиве
def getCountNumber(arrayIn):
    return max(list(map(lambda items: len(str(max(items))), arrayIn)))
    
# Напечатать двумерный массив в красивом виде
def printArray(arrayIn):
    countSymbol = getCountNumber(arrayIn)
    # каждая строка с элементами будет содержать стенку "|" между ними, а до стенки будет минимум 1 пробел, т.е. в виде: | 123 | 456 | ...,
    # сформируем на основе этого строку-разделитель
    rowSeparator = '|' + '-'.rjust((countSymbol + 2) * len(arrayIn[0]) + len(arrayIn[0]) -1, '-') + '|'

    for row in arrayIn:
        print(rowSeparator)
        strRow = "|"
        for column in row:
            strRow += ' ' + str(column).rjust(countSymbol, ' ') + " |"
        print(strRow)
    print(rowSeparator)

# Получить номер строки и столбца из порядкового элемента массива
def getRowAndColumn(position, countColumns):
    result = []
    result.append(position // countColumns)
    result.append(position % countColumns)
    return result

# Перемешать двумерный массив
def getMixArray(arrayIn):
    countColumns = len(arrayIn[0])
    result = arrayIn
    size = len(arrayIn) * countColumns
    fromPosition = 0
    tmpIndex = [ind for ind in range(int(size / 2), size)]
    fromToPositions = []
    while len(tmpIndex) > 0:
        toPosition = choice(tmpIndex)
        tmpIndex.remove(toPosition)
        # меняем элементы местами
        fromCell = getRowAndColumn(fromPosition, countColumns)
        toCell = getRowAndColumn(toPosition, countColumns)
        tmp = result[fromCell[0]][fromCell[1]]
        result[fromCell[0]][fromCell[1]] = result[toCell[0]][toCell[1]]
        result[toCell[0]][toCell[1]] = tmp

        fromToPositions.append([fromPosition, toPosition])
        fromPosition += 1
    print(f'\nПеремещения [с, на]: {fromToPositions}')
    return result

# ожидаем ввод корректного размера массива
check = True
while check:
    arraySize = [int(v) for v in input('Введите размер двумерного массива через пробел: ').split()]
    check = arraySize[0] * arraySize[1] % 2 != 0
    if (check):
        print('Количество элементов в массиве должно быть четным')

# наполняем массив случайными числами
arrayRaw = []
for i in range(arraySize[0]):
    arrayRaw.append([randint(1, 200) for _ in range(arraySize[1])])
    
print('\nИсходный массив:')
printArray(arrayRaw)
arrayMix = getMixArray(arrayRaw)
print('\nПеремешанный массив:')
printArray(arrayMix)