# Хранение телефонного справочника в Json-файле

import json
import consts
from repository.RepositoryBase import RepositoryBase

class Repository(RepositoryBase):

    __fileName = "repository/phones.json"
    __phones = []

    def loadData():
        """Загрузка телефонного справочника"""

        with open(Repository.__fileName, 'r', encoding='utf-8') as f:
            Repository.__phones = json.load(f)

    def saveData():
        """Сохранение телефонного справочника"""

        with open(Repository.__fileName, 'w', encoding="utf-8") as f:
            f.write(json.dumps(Repository.__phones, ensure_ascii=False))

    def findByFirstNameAndPrint(value):
        """Поиск контактов по имени"""

        Repository.__findContacts(1, value)

    def findByLastNameAndPrint(value):
        """Поиск контактов по фамилии"""

        Repository.__findContacts(2, value)

    def findByNumberAndPrint(value):
        """Поиск контактов по номеру телефона""" 

        Repository.__findContacts(3, value)
    
    def addContact(firstName, lastName, surName, contactPhones): 
        """Добавление нового контакта.
        
        Arguments:
        firstName -- Имя контакта.
        lastName -- Фамилия контакта.
        surName -- Отчество контакта.
        contactPhones -- Список телефонов.
        """
        
        # формируем контакт
        contact = {
            consts.KEY_ID: Repository.__getNewID(),
            consts.KEY_FIRST_NAME: firstName,
            consts.KEY_LAST_NAME: lastName,
            consts.KEY_SURNAME: surName,
            consts.KEY_PHONES: contactPhones
        }
        Repository.__phones.append(contact)

    def getContact(id):
        """Получить контакт со всеми телефонами по идентификатору

        Arguments:
        id -- Идентификатор контакта.
        """

        for contact in Repository.__phones:
            if (contact[consts.KEY_ID] == id):
                return contact

        return None
    
    def updateContact(contact):
        """Обновить контакт.

        Arguments:
        contact -- Контакт для обновления.
        """

        # по факту, тут уже измененный контакт внутри curContact, т.к. именно он и менялся ранее
        for curContact in Repository.__phones:
            if (curContact[consts.KEY_ID] == contact[consts.KEY_ID]):
                curContact = contact
                break

    def deleteContactOnId(id):
        """Удалить контакт по идентификатору

        Arguments:
        id -- Идентификатор контакта для удаления.
        """

        position = -1
        for ind in range(len(Repository.__phones)):
            if (Repository.__phones[ind][consts.KEY_ID] == id):
                position = ind
        
        if (position >= 0):
            Repository.__phones.pop(position)

    
    # функция проверки номера в номерах контакта
    def __isPhoneExist(phones, phoneFind):
        for phone in phones:
            for _, value in phone.items():
                if phoneFind in value:
                    return True
        return False

    # Поиск контактов в телефонном справочнике
    def __findContacts(cmd, text):
        # Обходим всех контактов
        result = []
        for contact in Repository.__phones:
            isExists = False
            # Обходим данные по контакту
            for key, value in contact.items():
                # введенный текст для поиска есть в данных контакта
                if (key != consts.KEY_ID and key != consts.KEY_PHONES and text.upper() in value.upper()):
                    # Уточняем поиск по имени или фамилии
                    if (cmd == 1 and key == consts.KEY_FIRST_NAME) or (cmd == 2 and key == consts.KEY_LAST_NAME):
                        isExists = True
                
                # если по имени и фамилии ничего не нашли, то проверим по номеру телефона
                if (not isExists and cmd not in range(1, 3) and key == consts.KEY_PHONES):
                    isExists = Repository.__isPhoneExist(contact[consts.KEY_PHONES], text)
            
            # нашли нужный контакт
            if (isExists):
                result.append(contact)
                
        RepositoryBase.printContacts(result)

    # Получить новый идентификатор контакта
    def __getNewID():
        result = 0
        for contact in Repository.__phones:
            result = max(result, contact[consts.KEY_ID])

        return result +1