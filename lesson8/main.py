# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - 
# данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import funcs
import tkinter as ui

def consoleRun():
    # Постоянный цикл для работы справочника
    while True:
        try:
            funcs.printHelp()
            inputComand = int(input('Введите номер команды: '))

            if (not funcs.procCommand(inputComand)):
                break   
        except ValueError:
            print("Неизвестная команда")

def uiRun():
    root = ui.Tk()
    root.title('Телефонный справочник')
    root.geometry('600x300')
    # кнопка добавления нового контакта
    frameAddButton = ui.Frame()
    frameAddButton.grid(row = 0, column = 0)
    ui.Button(master = frameAddButton, text = 'Добавить контакт', command = __buttonAddAction).grid(row = 0, column = 0)

    # блок с фильтром контакта
    frameFilter = ui.Frame()
    frameFilter.grid(row = 1, column = 0, sticky = 'W')
    ui.Label(master = frameFilter, text = 'Фильтр поиска').grid(row = 0, column = 0, sticky = 'W')
    global entFilter
    entFilter = ui.Entry(master = frameFilter)
    entFilter.grid(row = 1, column = 0)
    ui.Button(master = frameFilter, text = 'Найти', command = __buttonFilterAction).grid(row = 1, column = 1)

    # список найденных контактов
    frameContacts = ui.Frame()
    frameContacts.grid(row = 2, column = 0, sticky = 'W')
    global lstBoxContacts
    lstBoxContacts = ui.Listbox(master = frameContacts, width = 30)
    lstBoxContacts.grid(row = 0, column = 0, sticky = 'W')
    scrollbarContacts = ui.Scrollbar(master = frameContacts, orient = 'vertical', command = lstBoxContacts.yview)
    scrollbarContacts.grid(row = 0, column = 1, sticky = 'WNS')
    lstBoxContacts['yscrollcommand'] = scrollbarContacts.set
    global contacts
    contacts = funcs.getAllContacts()
    __updateContactsInList()

    # кнопки удаления и просмотра контакта
    frameButton = ui.Frame()
    frameButton.grid(row = 3, column = 0, sticky = 'E')
    ui.Button(master = frameButton, text = 'Показать', command = __buttonShowAction).grid(row = 0, column = 0)
    ui.Button(master = frameButton, text = 'Удалить', command = __buttonDeleteAction).grid(row = 0, column = 1)

    # блок отображения данных по контакту
    global frameContactData
    frameContactData = ui.Frame()
    frameContactData.grid(row = 0, column = 1, rowspan = 4, sticky = 'NSE')

    root.mainloop()

# Наполнение списка контактами
def __updateContactsInList():
    contactsFIO = funcs.contactsToContactsFIO(contacts)
    lstBoxContacts.delete(0, 'end')
    for contact in contactsFIO:
        lstBoxContacts.insert('end', contact)

# Обработка кнопки поиска в фильтре
def __buttonFilterAction():
    filterText = entFilter.get()
    global contacts
    contacts = funcs.findAllContactsOnFilter(filterText)
    __updateContactsInList()
    __clearContactData()

# Обработка кнопки отображения данных по контакту
def __buttonShowAction():
    selection = lstBoxContacts.curselection()[0]
    contact = contacts[selection]
    contactData = funcs.getContactDataAsString(contact)
    __clearContactData()
    for ind, row in enumerate(contactData):
        ui.Label(master = frameContactData, text = row).grid(row = ind, column = 0, sticky = 'W')


# Обработка кнопки удаления контакта
def __buttonDeleteAction():
    selection = lstBoxContacts.curselection()[0]
    global contacts
    contact = contacts[selection]
    funcs.deleteContact(contact)
    contacts = funcs.getAllContacts()
    __updateContactsInList()
    __clearContactData()

# Обработка кнопки добавления нового контакта
def __buttonAddAction():
    root = ui.Toplevel()
    root.title('Контакт')

    # Блок ввода имени, фамилии и отчества
    frameFIO = ui.Frame(root)
    frameFIO.grid(row = 0, column = 0, sticky = 'NW')
    ui.Label(master = frameFIO, text = 'Имя').grid(row = 0, column = 0, sticky = 'W')
    entFirstName = ui.Entry(master = frameFIO)
    entFirstName.grid(row = 0, column = 1)
    ui.Label(master = frameFIO, text = 'Фамилия').grid(row = 1, column = 0, sticky = 'W')
    entLastName = ui.Entry(master = frameFIO)
    entLastName.grid(row = 1, column = 1)
    ui.Label(master = frameFIO, text = 'Отчество').grid(row = 2, column = 0, sticky = 'W')
    entSurName = ui.Entry(master = frameFIO)
    entSurName.grid(row = 2, column = 1)

    # Блок добавления номеров
    uiPhones = []
    framePhone = ui.Frame(root)
    framePhone.grid(row = 0, column = 1, sticky = 'N')
    framePhoneBlock = ui.Frame(framePhone)
    ui.Button(master = framePhone, text = 'Добавить номер', command = lambda: __addBlockPhone(framePhoneBlock, uiPhones)).grid(row = 0, column = 0)
    framePhoneBlock.grid(row = 1, column = 0, sticky = 'N')    
    __addBlockPhone(framePhoneBlock, uiPhones)

    # Кнопка сохранения
    buttonSave = ui.Button(master = root, text = 'Сохранить', command = lambda: __saveContact(entFirstName.get(), entLastName.get(), entSurName.get(), uiPhones, root))
    buttonSave.grid(row = 1, column = 0, columnspan = 2)
    
# Очистка блока с данными по контакту
def __clearContactData():
    for widget in frameContactData.winfo_children():
       widget.destroy()
    frameContactData.pack_forget()

# Обработка кнопки добавления нового номера телефона в окне добавления контакта
def __addBlockPhone(phoneBlock, uiPhones):
    framePhoneRow = ui.Frame(phoneBlock)
    ui.Label(master = framePhoneRow, text = 'Описание').grid(row = 0, column = 0, sticky = 'W')
    entPhoneTitle = ui.Entry(master = framePhoneRow)
    entPhoneTitle.grid(row = 0, column = 1)
    ui.Label(master = framePhoneRow, text = 'Номер').grid(row = 1, column = 0, sticky = 'W')
    entPhone = ui.Entry(master = framePhoneRow)
    entPhone.grid(row = 1, column = 1)
    uiPhones.append([entPhoneTitle, entPhone])
    framePhoneRow.pack()

# Сохранение нового контакта (без проверок)
def __saveContact(firstName, lastName, surName, uiPhones, window):
    # сформируем список номеров
    phones = list(map(lambda item: [item[0].get(), item[1].get()], uiPhones))
    funcs.addContact(firstName, lastName, surName, phones)
    window.destroy()
    global contacts
    contacts = funcs.getAllContacts()
    __updateContactsInList()
    __clearContactData()


#############################################
# Основная программа

# Загружаем телефонный справочник
funcs.loadData()

# Запуск программы в консольном режиме
#consoleRun()

# Запуск программы с графическим интерфейсом
uiRun()
#############################################