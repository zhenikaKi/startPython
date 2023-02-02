
'''
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
import random
n = int(input('Введите N: '))
#lst = [random.randint(1, 10) for ind in range(n)]
#x = lst[len(lst)-1]
lst = []
for ind in range(1, n+1):
    lst.append(int(input(f'Введите {ind}-ый элемент массива: ')))
x = int(input('Введите X: '))
count = 0
for value in lst:
    if (value == x):
        count += 1
print(lst)
print(f'Кол-во: {count}')
'''

'''
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
n = int(input('Введите N: '))
lst = []
for ind in range(1, n+1):
    lst.append(int(input(f'Введите {ind}-ый элемент массива: ')))
x = int(input('Введите X: '))
result = x
difference = x
for value in lst:
    newDifference = abs(value - x)
    if newDifference < difference:
        result = value
        difference = newDifference
print(f'Ближайшее число: {result}')
'''

'''
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так: ...
# А русские буквы оцениваются так: ...
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
en = [{'AEIOULNSTR': 1}, {'DG': 2}, {'BCMP': 3}, {'FHVWY': 4}, {'K': 5}, {'JX': 8}, {'QZ': 10}]
ru = [{'АВЕИНОРСТ': 1}, {'ДКЛМПУ': 2}, {'БГЁЬЯ': 3}, {'ЙЫ': 4}, {'ЖЗХЦЧ': 5}, {'ШЭЮ': 8}, {'ФЩЪ': 10}]
word = input('Введите слово: ').upper()
# определим язык по первой букве
curLang = ru
for item in en:
    for key, _ in item.items():
        if word[0] in key:
            curLang = en
            break

result = 0
for item in curLang:
    for key, value in item.items():
        for symbol in word:
            print(f'key = {key}, symbol = {symbol}')
            if (symbol in key):
                result += value
print (f'Стоимость слова: {result}')
'''

# Задача HARD необязательная
# Имеется список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
lst = [2, 6, 3, 4, 8, 7, 6 , 3 , 4]
#lst = input('Введите числа через пробел: ').split()
#lst = [int(ind) for ind in lst]
# сперва найдем все последовательности. В ключе будет размер последовательности,
# а в значении - список диапазонов последовательности этого размера
minMax = {}
maxSequence = 0
for value1 in lst:
    newMinMax = [value1, value1]
    isUpdateMax = True
    while isUpdateMax:
        # изначально предполагаем, что после обхода всех элементов не будет нового возрастающего элемента
        isUpdateMax = False
        for value2 in lst:
            if value2 - newMinMax[1] == 1:
                newMinMax[1] = value2
                # нашли новый элемент в последовательности, а значит нужно еще раз пройтись по всем элементам,
                # чтобы проверить новую последовательность
                isUpdateMax = True
    sequence = newMinMax[1] - newMinMax[0]
    if sequence > 0:
        if (sequence in minMax):
            sequenceRanges = minMax[sequence]
        else:
            sequenceRanges = []
        sequenceRanges.append(newMinMax)
        minMax[sequence] = sequenceRanges
    # сразу определяем размер максимальной последовательности
    maxSequence = max(sequence, maxSequence)

# выводим все найденные максимальные последовательности
print('Все последовательности:')
print(minMax)
for (size, value) in minMax.items():
    if (size == maxSequence):
        print(f'Максимальные последовательности: {value}')