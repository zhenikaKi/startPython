# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
'''
a = int(input('Введите A: '))
b = int(input('Введите B: '))

def stepen(value, ind):
    if (ind >= b):
        return value
    return value * stepen(value, ind +1)

result = stepen(a, 1)
print(result)
'''

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
'''
a = int(input('Введите A: '))
b = int(input('Введите B: '))

def sumR(a, b):
    if (b <= 0):
        return a
    return sumR(a +1, b -1)

result = sumR(a, b)
print(result)
'''

# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями вычисления
# таких выражений нельзя, если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел.
# Надо посчитать результат введенного выражения.
# Например, на входе 1+9/3*7-4
# на выходе 18
strIn = input('Введите строку для подсчета (операции +-/*): ')

fakeSymbol = "~"
# выполнение математических операций в строке с возможностью пропуска операций
def calcWithIgnore(strIn, strInOut, ind, left, oper, right, ignoreSymbols):
    if (ind > len(strIn)):
        if left != fakeSymbol:
            strInOut += left
        if oper != fakeSymbol:
            strInOut += oper
        if right != fakeSymbol:
            strInOut += right
        return strInOut
    if ind == len(strIn):
        symbol = ""
    else:
        symbol = strIn[ind]
    newInd = ind +1
    if symbol in "/*+-" or symbol == "":
        # определяем после какого именно числа стоит арифметическая операция
        # до этой операции мы заполняли левое число
        if symbol != "" and left != fakeSymbol and oper == fakeSymbol and right == fakeSymbol:
            # при необходимости пропускаем операцию
            if symbol in ignoreSymbols:
                strInOut += left + symbol
                left = ""
                right = fakeSymbol
                oper = fakeSymbol
            # или начинаем собирать правое число
            else:
                right = ""
                oper = symbol
        #до этого собирали правое число
        elif (left != fakeSymbol and oper != fakeSymbol and right != fakeSymbol):
            if oper == "/":
                res = float(left) / float(right)
            elif oper == "*":
                res = float(left) * float(right)
            elif oper == "+":
                res = float(left) + float(right)
            else:
                res = float(left) - float(right)
            strInOut += str(res) + symbol
            
            # после выполненной операции вновь просматриваем строку сначала, чтобы не нарушить правила выполнения операций
            strIn = strInOut + strIn[newInd:]
            strInOut = ""
            newInd = 0         
            left = ""
            right = fakeSymbol
            oper = fakeSymbol
    elif right == fakeSymbol:
        left += symbol
    else:
        right += symbol
    
    #print(f"[{ind}]: strIn = {strIn}, symbol = {symbol}, left = {left}, oper = {oper}, right = {right}, strInOut = {strInOut}")

    return calcWithIgnore(strIn, strInOut, newInd, left, oper, right, ignoreSymbols)

# вычисление всех операций
def calcAllOperattion(strIn, ignoreSymbols):
    # арифметических операций больше нет в строке
    if "/" not in strIn and "*" not in strIn and "+" not in strIn and "-" not in strIn:
        return strIn
    # в строке закончились операции умножения и деления, дальше считаем все оставшиеся
    if ignoreSymbols != "" and "/" not in strIn and "*" not in strIn:
        return calcAllOperattion(strIn, "")
    newStep = calcWithIgnore(strIn, "", 0, "", fakeSymbol, fakeSymbol, ignoreSymbols)
    return calcAllOperattion(newStep, ignoreSymbols)

# стартовая функция для подсчета
def calcStr(strIn):
    # начинаем подсчет с игнорирования операций сложения и вычитания
    return calcAllOperattion(strIn, "+-")

strOut = calcStr(strIn)
print(f'{strIn} = {strOut}')