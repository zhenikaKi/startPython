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

    def addContact(firstName, lastName, surName, phones): 
        """Добавление нового контакта.
        
        Arguments:
        firstName -- Имя контакта.
        lastName -- Фамилия контакта.
        surName -- Отчество контакта.
        phones -- Список телефонов. Каждый элемент состоит из массива, на первом месте заголовок номера, на втором - номер телефона.
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