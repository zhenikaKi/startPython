
import consts

class RepositoryBase:
    """Базовый класс по работе с хранилищем телефонных номеров"""

    def loadData():
        """Загрузка телефонного справочника"""
        pass
    
    def saveData():
        """Сохранение телефонного справочника"""
        pass

    def findByFirstName(value):
        """Поиск контактов по имени"""
        pass

    def findByLastName(value):
        """Поиск контактов по фамилии"""
        pass

    def findByNumber(value):
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

    def getAllContacts():
        """Получить список контактов"""
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