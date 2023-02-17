# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам

'''
# количество гласных букв в фразе
def getCountVowels(strIn):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    isVowels = lambda w: w in vowels

    return len(list(filter(lambda v: v == True, map(isVowels, strIn))))

strArray = input('Введите стихотворение: ').split()
countDistinctVowels = len(set(list(map(lambda w: getCountVowels(w), strArray))))
print('Парам пам-пам' if countDistinctVowels == 1 else 'Пам парам')
'''


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

'''
def print_operation_table(operation, num_rows=6, num_columns=6):
    maxLength = len(str(num_rows * num_columns))
    for i in range(1, num_rows +1):
        strTmp = ''
        for j in range(1, num_columns +1):
            value = str(operation(i, j))
            strTmp += value.rjust(maxLength, ' ') + '  '
        print(strTmp)

print_operation_table(lambda x, y: x * y, 8, 7)
'''


# Необязательное задание
# Сделать локальный чат-бот с хранилищем данных в формате JSON, как объясняли в приложенной записи буткемпа.
import json

fileName = "setting.json"

# Системные команды
sysCommands = {
    '/start': {
        'message': 'Бот с возможностью добавления своих команд. Список всех команд можно получить с помощью /help',
        'help': 'Начальная команда бота'
    },
    '/help': {
        'command': 'generateHelp',
        'help': 'Текущая справка'
    },
    '/close': {
        'command': 'closeBot',
        'help': 'Выход из бота'
    },
    '/add': {
        'command': 'addComand',
        'help': 'Добавление новой текстовой команды'
    },
    '/edit': {
        'command': 'editComand',
        'help': 'Редактирование текстовой команды'
    }
}
# Пользовательские команды
userCommands = {}

# Сформировать текст справки
def generateHelp():
    result = ''
    for key, value in sysCommands.items():
        result += key + ': ' + value['help'] + '\n'
    for key, value in userCommands.items():
        result += key + ': ' + value['help'] + '\n'
    return result

# Добавление пользовательской команды
def addComand():
    cmd = ''
    isExists = False
    while len(cmd) == 0 or isExists:
        cmd = input('Введите новую команду: /')
        isExists = cmd in sysCommands or cmd in userCommands
        if (isExists):
            print('Команда уже существует!')
    help = input('Введите описание команды: ')
    message = input('Введите ответ, который бот пришлет на команду: ')

    userCommands[f'/{cmd}'] = {'message': message, 'help': help}
    print('Команда добавлена')

# Изменение пользовательской команды
def editComand():
    cmd = ''
    isExists = False
    while not isExists:
        cmd = input('Введите команду для изменения: /')
        cmd = '/' + cmd
        isExists = cmd in userCommands
        if (not isExists):
            print('Команда не найдена!')
    cmdData = userCommands[cmd]
    print('Текущее описание: ' + cmdData['help'])
    help = input('Введите новое описание команды: ')
    print('Текущий ответ: ' + cmdData['message'])
    message = input('Введите новый ответ на команду: ')

    userCommands[cmd] = {'message': message, 'help': help}
    print('Команда обновлена')

# Обработка системных команд
def procSysCommand(cmdIn):
    if cmdIn in sysCommands:
        cmdData = sysCommands[cmdIn]
        if 'message' in cmdData:
            print(cmdData['message'])
            return 1
        elif 'command' in cmdData:
            result = 1
            cmd = cmdData['command']
            if cmd == 'generateHelp':
                print(generateHelp())
            if cmd == 'addComand':
                addComand()
            if cmd == 'editComand':
                editComand()
            elif cmd == 'closeBot':
                result = -1
            else:
                result = 0
            return result
    return 0

# Оработка пользовательских команд
def procUserCommand(cmdIn):
    if cmdIn in userCommands:
        cmdData = userCommands[cmdIn]
        if 'message' in cmdData:
            print(cmdData['message'])
            return True
    return False

# Сохранение данных
def saveData():
    with open(fileName, 'w', encoding="utf-8") as f:
        f.write(json.dumps(userCommands, ensure_ascii=False))

# Загрузка данных
def loadData():
    with open(fileName, 'r', encoding='utf-8') as f:
        return json.load(f)

userCommands = loadData()
while True:
    inputComand = input('Введите команду: ')
    resultSysCommand = procSysCommand(inputComand)

    # нужно выйти из бота
    if resultSysCommand == -1:
        saveData()
        break
    # обработали системную команду
    elif resultSysCommand == 1:
        continue

    # обрабатываем пользовательскую команду
    if procUserCommand(inputComand) == False:
        print('Некорректная команда')
