
import consts

class RepositoryBase:
    """Базовый класс по работе с хранилищем телефонных номеров"""

    def loadData():
        """Загрузка телефонного справочника"""
        pass
    
    def saveData():
        """Сохранение телефонного справочника"""
        pass

    def findByFirstNameAndPrint(value):
        """Поиск контактов по имени"""
        pass

    def findByLastNameAndPrint(value):
        """Поиск контактов по фамилии"""
        pass

    def findByNumberAndPrint(value):
        """Поиск контактов по номеру телефона""" 
        pass

    def addContact(firstName, lastName, surName, contactPhones): 
        """Добавление нового контакта.
        
        Arguments:
        firstName -- Имя контакта.
        lastName -- Фамилия контакта.
        surName -- Отчество контакта.
        contactPhones -- Список телефонов.
        """
        pass

    def getContact(id):
        """Получить контакт со всеми телефонами по идентификатору

        Arguments:
        id -- Идентификатор контакта.
        """
        pass

    def updateContact(contact):
        """Обновить контакт.

        Arguments:
        contact -- Контакт для обновления.
        """
        pass

    def deleteContactOnId(id):
        """Удалить контакт по идентификатору

        Arguments:
        id -- Идентификатор контакта для удаления.
        """
        pass

    # Печать контакта в красивом виде
    def printContacts(contacts):
        print('Найденные контакты:')
        for contact in contacts:
            text = f"[{contact[consts.KEY_ID]}] {contact[consts.KEY_FIRST_NAME]} {contact[consts.KEY_LAST_NAME]} {contact[consts.KEY_SURNAME]}: "
            phones = contact[consts.KEY_PHONES]
            for ind in range(len(phones)):
                if ind > 0:
                    text += ', '
                text += f"{phones[ind][consts.KEY_TITLE]} {phones[ind][consts.KEY_NUMBER]}"
            print(text)