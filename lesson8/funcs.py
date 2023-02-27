
import consts
#from repository.JsonRepository import Repository # Хранилище в json-файле
from repository.SqliteRepository import Repository # Хранилище в БД

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

# Получить все контакты
def getAllContacts():
    return Repository.getAllContacts()
    return True

# Преобразовать контакты к списку ФИО контактов
def contactsToContactsFIO(contacts):
    result = list(map(lambda item: f'{item[consts.KEY_FIRST_NAME]} {item[consts.KEY_LAST_NAME]} {item[consts.KEY_SURNAME]}', contacts))
    return result

# Получить данные по контакту в виде списка строк, готовых для отображения
def getContactDataAsString(contact):
    contactData = Repository.getContact(contact[consts.KEY_ID])
    result = []
    result.append(f'Имя: {contactData[consts.KEY_FIRST_NAME]}')
    result.append(f'Фамилия: {contactData[consts.KEY_LAST_NAME]}')
    result.append(f'Отчество: {contactData[consts.KEY_SURNAME]}')
    result.append('')

    for contact in contactData[consts.KEY_PHONES]:
        result.append(f'{contact[consts.KEY_TITLE]}: {contact[consts.KEY_NUMBER]}')
    
    return result

# Удалить контакт
def deleteContact(contact):
    Repository.deleteContactOnId(contact[consts.KEY_ID])

# Найти все контакты по фильтру
def findAllContactsOnFilter(filterText):
    contacts = []
    contacts.extend(Repository.findByFirstName(filterText))
    contacts.extend(Repository.findByLastName(filterText))
    contacts.extend(Repository.findByNumber(filterText))
    distinctContacts = []
    for contact in contacts:
        if (contact == None):
            continue
        distinctContactsId = list(map(lambda item: item[consts.KEY_ID], distinctContacts))
        if contact[consts.KEY_ID] not in distinctContactsId:
            distinctContacts.append(contact)
    return distinctContacts

# Добавление нового контакта
def addContact(firstName, lastName, surName, phones):
    # формируем список номеров
    contactPhones = list(map(lambda item: {consts.KEY_TITLE: item[0], consts.KEY_NUMBER: item[1]}, phones))   
    Repository.addContact(firstName, lastName, surName, contactPhones)

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
        contacts = Repository.findByFirstName(text)
    elif cmd == __CMD_FIND_BY_LAST_NAME:
        contacts = Repository.findByLastName(text)
    else:
        contacts = Repository.findByNumber(text)

    __printContacts(contacts)

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
    addContact(firstName, lastName, surName, phones)

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



# Печать контакта в красивом виде
def __printContacts(contacts):
    print('Найденные контакты:')
    for contact in contacts:
        text = f"[{contact[consts.KEY_ID]}] {contact[consts.KEY_FIRST_NAME]} {contact[consts.KEY_LAST_NAME]} {contact[consts.KEY_SURNAME]}: "
        phones = contact[consts.KEY_PHONES]
        for ind in range(len(phones)):
            if ind > 0:
                text += ', '
            text += f"{phones[ind][consts.KEY_TITLE]} {phones[ind][consts.KEY_NUMBER]}"
        print(text)