
import consts
from repository.JsonRepository import Repository # Хранилище в json-файле

__CMD_FIND_BY_FISRT_NAME = 1
__CMD_FIND_BY_LAST_NAME = 2

# Загрузка телефонного справочника
def loadData():
    Repository.loadData()

# Напечатать справку по командам
def printHelp():
    strHelp = f'''-----------------------------------------
{__CMD_FIND_BY_FISRT_NAME} - поиск по имени контакта
{__CMD_FIND_BY_LAST_NAME} - поиск по фамилии контакта
3 - поиск по номеру телефона
4 - Добавление нового контакта (без проверки на существование)
5 - Редактирование контакта
6 - Удаление контакта
0 - выход
'''
    print(strHelp)


# Обработка команды
def procCommand(cmd):
    if cmd == 0:
        Repository.saveData()
        return False
    elif cmd in range(1, 4):
        __findContacts(cmd)
    elif cmd == 4:
        __addContact()
    elif cmd == 5:
        __findContactForEdit()
    elif cmd == 6:
        __deleteContact()
    else:
        print("Неизвестная команда")
    return True

# Поиск контактов в телефонном справочнике
def __findContacts(cmd):
    strHelp = 'Введите '
    if cmd == __CMD_FIND_BY_FISRT_NAME:
        strHelp += 'имя контакта: '
    elif cmd == __CMD_FIND_BY_LAST_NAME:
        strHelp += 'фамилию контакта: '
    else:
        strHelp += 'номер телефона: '
    text = input(strHelp)

    if cmd == __CMD_FIND_BY_FISRT_NAME:
        Repository.findByFirstNameAndPrint(text)
    elif cmd == __CMD_FIND_BY_LAST_NAME:
        Repository.findByLastNameAndPrint(text)
    else:
        Repository.findByNumberAndPrint(text)

# Добавление нового контакта
def __addContact():
    firstName = input('Имя контакта: ')
    lastName = input('Фамилия контакта: ')
    surName = input('Отчество контакта: ')
    print('Добавление телефонов (введите 0 для завершения):')
    phones = []
    while True:
        phone = input('Номер телефона: ')
        title = input('Описание номера: ')
        if phone == '0' or title == '0':
            break
        phones.append([title, phone])
    
    Repository.addContact(firstName, lastName, surName, phones)

# Поиск контакта для дальнейшего редактирования
def __findContactForEdit():
    while True:
        try:
            id = int(input('Введите идентификатор контакта: '))
            contact = Repository.getContact(id)
            if (contact != None):
                __editContact(contact)
                break
            else:
                print("Некорректный идентификатор")
        except ValueError:
            print("Некорректный идентификатор")

# Редактирование контакта
def __editContact(contact):
    contact[consts.KEY_FIRST_NAME] = input(f'Текущее имя "{contact[consts.KEY_FIRST_NAME]}", новое: ')
    contact[consts.KEY_LAST_NAME] = input(f'Текущая фамилия "{contact[consts.KEY_LAST_NAME]}", новая: ')
    contact[consts.KEY_SURNAME] = input(f'Текущее отчество "{contact[consts.KEY_SURNAME]}", новое: ')

    for phone in contact[consts.KEY_PHONES]:
        phone[consts.KEY_NUMBER] = input(f'Текущий номер ({phone[consts.KEY_TITLE]}) "{phone[consts.KEY_NUMBER]}", новый: ')
    Repository.updateContact(contact)
    print('Контакт изменен')

# Удаление контакта
def __deleteContact():
    while True:
        try:
            id = int(input('Введите идентификатор контакта для удаления: '))
            if (Repository.getContact(id) != None):
                Repository.deleteContactOnId(id)
                print("Контакт удален")
                break
            else:
                print("Некорректный идентификатор")
        except ValueError:
            print("Некорректный идентификатор")