
'''
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
n = int(input('Введите количество монет: '))
countTails = 0
countEagle = 0
for ind in range(1, n +1):
    side = int(input('Введите 0, если монета #{} лежит решкой вверх, или 1, если она лежит гербом вверх: '.format(ind)))
    if side == 0:
        countTails += 1
    else:
        countEagle += 1
if countTails < countEagle:
    print('Монеты решкой вверх нужно перевернуть {} раз'.format(countTails))
elif countEagle < countTails:
    print('Монеты гербом вверх нужно перевернуть {} раз'.format(countEagle))
else:
    print('Можно перевернуть монеты, которые лежат на любой стороне')
'''

'''
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет
# сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#4 4 -> 2 2
#5 6 -> 2 3
import math
s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
#Считаем по формуле кв.уравнения: y^2 - s*y + p = 0
d = s**2 - 4 * p
if d >= 0:
    x = (s + math.sqrt(d)) / 2
    y = s - x
    print('Загаданные числа: {} и {}'.format(x, y))
else:
    print('Загаданны некорректные данные')
'''

'''
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
n = int(input('Введите N: '))
for i in range(n):
    value = 2 ** i
    if (value > n):
        break
    print(value)
'''

'''
# Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . Но теперь количество предикатов не три,
# а генерируется случайным образом от 5 до 25, сами значения предикатов случайные,
# проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени
# отработала программа. В конце вывести результат проверки истинности этого утверждения.
# ¬ - not, ⋁ - and, ⋀ - or
import time
from random import randint

start = time.time()
COUNT_ITER = 100
countSucces = 0
# цикл по итерациям проверки
for ind in range(COUNT_ITER):
    countPredicat = randint(5, 25)
    # цикл по количеству предикатов
    for predicatInd in range(countPredicat):
        predicatValue = bool(randint(0, 1))
        if predicatInd == 0:
            leftCheck = predicatValue
            rightCheck = not(predicatValue)
        else:
            leftCheck = leftCheck and predicatValue
            rightCheck = rightCheck or not(predicatValue)
    # итоговая проверка теоремы
    if (not(leftCheck) == rightCheck):
        countSucces += 1

end = time.time()
print('Во всех итерациях теорема доказана: {}, время: {}'.format((COUNT_ITER == countSucces), (end - start)))
'''

'''
# Задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('Введите K: '))
result = [0]
prev1 = 0
prev2 = 0
coef = 1
for ind in range(k):
    if ind == 0:
        prev2 = 1
    else:
        tmp = prev1
        prev1 = prev2
        prev2 = tmp + prev1
        coef = -1

    result.append(prev2)
    result.insert(0, prev2 * coef)
print(f'Числа Фибоначчи: {result}')
'''

# Задача 5 - HARD необязательная
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в N-мерном пространстве. Сначала задается N с клавиатуры, потом задаются координаты точек.
from math import sqrt
n = int(input('Введите N: '))
sumSquares = 0
for ind in range(1, n+1):
    p1 = int(input('Введите координаты 1 точки в {}-ом пространстве: '.format(ind)))
    p2 = int(input('Введите координаты 2 точки в {}-ом пространстве: '.format(ind)))
    sumSquares += (p2 - p1) ** 2
result = sqrt(sumSquares)
print(f'Расстояние: {result}')
