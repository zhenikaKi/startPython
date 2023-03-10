'''
# Задача 2: Найдите сумму цифр трехзначного числа.
value = int(input('Введите трехзначное число: '))
first = value // 100
value %= 100
second = value // 10
value %= 10
print('Сумма цифр: {}'.format(first + second + value))
'''

'''
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
s = int(input('Введите сделанное количество журавликов: '))
# Считаем уравнение: S = 2x + 2 * 2x, т.е. x = S / 6 (Это Петя и Сережа)
p = s // 6
k = s - p * 2
print('Петя и Сережа сделали по: {}, а Катя: {}'.format(p, k))
'''

'''
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
ticket = input('Введите номер билета: ')
# делаем без циклов с помощью строки
sumLeft = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sumRight = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if sumLeft == sumRight:
    print('Билет счастливый')
else:
    print('Билет несчастливый')
'''

'''
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
n = int(input('Введите размер шоколадки N: '))
m = int(input('Введите размер шоколадки M: '))
k = int(input('Введите количество долек: '))
if n % k == 0 or m % k == 0 or (n * m >= k and (k % n == 0 or k % m == 0)):
    print('Можно отломить {} долек зараз'.format(k))
else:
    print('Нельзя отломить {} долек зараз'.format(k))
'''

# Задача 2: - HARD необязательная, идет за 3 обязательных 
# Найдите сумму цифр любого вещественного или целого числа. 
# Можно использовать decimal. Через строку решать нельзя. 
from decimal import Decimal
value = Decimal(input('Введите вещественное (через точку) или целое число: '))
digits = value.as_tuple().digits
sum = 0
for digit in digits:
    sum += digit
print('Сумма цифр: {}'.format(sum))