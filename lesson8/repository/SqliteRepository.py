# Хранение телефонного справочника в БД Sqlite

import sqlite3
import consts
from repository.RepositoryBase import RepositoryBase

class Repository(RepositoryBase):

    __db = sqlite3.connect('repository/phones.db')

    def loadData():
        """Загрузка телефонного справочника"""
        Repository.__initDb()

    def findByFirstNameAndPrint(value):
        result = Repository.__getContactsFromDb(f"{consts.KEY_DB_FIRST_NAME} like '%{value}%'")
        RepositoryBase.printContacts(result)

    def findByLastNameAndPrint(value):
        """Поиск контактов по фамилии"""
        result = Repository.__getContactsFromDb(f"{consts.KEY_DB_LAST_NAME} like '%{value}%'")
        RepositoryBase.printContacts(result)

    def findByNumberAndPrint(value):
        """Поиск контактов по номеру телефона""" 
        result = Repository.__getContactsFromDb(f"{consts.KEY_NUMBER} like '%{value}%'")
        RepositoryBase.printContacts(result)

    def addContact(firstName, lastName, surName, contactPhones): 
        """Добавление нового контакта.
        
        Arguments:
        firstName -- Имя контакта.
        lastName -- Фамилия контакта.
        surName -- Отчество контакта.
        contactPhones -- Список телефонов.
        """

        # добавляем контакт
        sql = f"""insert into {consts.TABLE_CONTACTS} ({consts.KEY_DB_FIRST_NAME}, {consts.KEY_DB_LAST_NAME}, {consts.KEY_SURNAME}) 
            values (?, ?, ?)"""
        parameters = (firstName, lastName, surName)
        cursor = Repository.__db.cursor()
        cursor.execute(sql, parameters)
        Repository.__db.commit()
        id = cursor.lastrowid

        # добавляем номера телефонов
        sql = f"""insert into {consts.TABLE_PHONES} ({consts.KEY_DB_CONTACT_ID}, {consts.KEY_TITLE}, {consts.KEY_NUMBER}) 
            values (?, ?, ?)"""
        for phone in contactPhones:
            parameters = (id, phone[consts.KEY_TITLE], phone[consts.KEY_NUMBER])
            Repository.__db.execute(sql, parameters)
        Repository.__db.commit()

    def getContact(id):
        """Получить контакт со всеми телефонами по идентификатору

        Arguments:
        id -- Идентификатор контакта.
        """
        result = Repository.__getContactsFromDb(f"{consts.KEY_ID} = {id}")
        if (len(result) > 0):
            return result[0]
        
        return None

    def updateContact(contact):
        """Обновить контакт.

        Arguments:
        contact -- Контакт для обновления.
        """
        # Обновляем контакт
        sql = f"""update {consts.TABLE_CONTACTS} 
            set {consts.KEY_DB_FIRST_NAME} = ?,
            {consts.KEY_DB_LAST_NAME} = ?,
            {consts.KEY_SURNAME} = ?
            where {consts.KEY_ID} = {contact[consts.KEY_ID]}"""
        parameters = (contact[consts.KEY_FIRST_NAME], contact[consts.KEY_LAST_NAME], contact[consts.KEY_SURNAME])
        Repository.__db.execute(sql, parameters)

        # Обновляем номера
        for phone in contact[consts.KEY_PHONES]:
            sql = f"""update {consts.TABLE_PHONES} 
                set {consts.KEY_TITLE} = ?,
                {consts.KEY_NUMBER} = ?
                where {consts.KEY_DB_PHONE_ID} = {phone[consts.KEY_PHONE_ID]}"""
            parameters = (phone[consts.KEY_TITLE], phone[consts.KEY_NUMBER])
            Repository.__db.execute(sql, parameters)
        Repository.__db.commit()

    def deleteContactOnId(id):
        """Удалить контакт по идентификатору

        Arguments:
        id -- Идентификатор контакта для удаления.
        """
        Repository.__db.execute(f"delete from {consts.TABLE_CONTACTS} where {consts.KEY_ID} = {id}")
        Repository.__db.commit()

    def __initDb():
        Repository.__db.execute('PRAGMA foreign_keys=on;')
        Repository.__db.execute(f"""create table if not exists {consts.TABLE_CONTACTS} (
        {consts.KEY_ID} integer primary key autoincrement,
        {consts.KEY_DB_FIRST_NAME} text,
        {consts.KEY_DB_LAST_NAME} text,
        {consts.KEY_SURNAME} text
        )""")
        Repository.__db.execute(f"""create table if not exists {consts.TABLE_PHONES} (
        {consts.KEY_DB_PHONE_ID} integer primary key autoincrement,
        {consts.KEY_DB_CONTACT_ID} integer not null,
        {consts.KEY_TITLE} text,
        {consts.KEY_NUMBER} text,
        foreign key ({consts.KEY_DB_CONTACT_ID}) references {consts.TABLE_CONTACTS}({consts.KEY_ID}) on delete cascade
        )""")
        
    # Получить контакты и их номера из базы с использованием доп.условия
    # Важно: В sqllite нет функций приведения к верхнему/нижнему регистрам, поиск будет регистрозависемым
    def __getContactsFromDb(condition):
        sql = f"""select c.*, 
                    p.{consts.KEY_DB_PHONE_ID}, 
                    p.{consts.KEY_TITLE}, 
                    p.{consts.KEY_NUMBER}  
            from {consts.TABLE_CONTACTS} c,
                {consts.TABLE_PHONES} p
            where c.{consts.KEY_ID} = p.{consts.KEY_DB_CONTACT_ID} 
               and {condition}
            order by c.{consts.KEY_ID}, p.{consts.KEY_DB_PHONE_ID}
        """
        cursor = Repository.__db.execute(sql)
        result = []
        oldId = -1
        contact = None
        for row in cursor:
            # Сменился контакт
            if (oldId != row[0]):
                # Сохраняем предыдущий контакт
                if (contact != None):
                    result.append(contact)

                contact = {
                    consts.KEY_ID: row[0],
                    consts.KEY_FIRST_NAME: row[1],
                    consts.KEY_LAST_NAME: row[2],
                    consts.KEY_SURNAME: row[3],
                    consts.KEY_PHONES: []
                }
                oldId = row[0]
            
            # Добавляем номера
            contact[consts.KEY_PHONES].append({
                consts.KEY_PHONE_ID: row[4],
                consts.KEY_TITLE: row[5],
                consts.KEY_NUMBER: row[6]
            })
        result.append(contact)
        return result