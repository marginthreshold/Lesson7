import view
import codecs


def create_contact():
    view.ask_to_fill("номер телефона")
    create_contact_number = view.get_contact_info()
    view.ask_to_fill("фамилию")
    create_contact_surname = view.get_contact_info()
    view.ask_to_fill("имя")
    create_contact_name = view.get_contact_info()
    view.ask_to_fill("комментарии")
    create_contact_comments = view.get_contact_info()
    create_contact_list = [[create_contact_surname, create_contact_name,
                           create_contact_number, create_contact_comments]]
    return create_contact_list


def add_to_all_contacts(contact_list, contact_file_name, write_method,sep):
    with codecs.open(contact_file_name, write_method, "utf-8") as all_contacts_file:
        for line in contact_list:
            all_contacts_file.writelines(sep.join(list(map(str, line))))
            all_contacts_file.writelines("\n")


def from_row_file_to_list(file_name):
    with codecs.open(file_name, "r", "utf-8") as file:
        list_from_file = list(file.read().split())
    new_list = []
    for i in list_from_file:
        new_list.append(list(i.split(";")))
    new_list.pop(0)
    return new_list


def from_column_file_to_list(file_name):
    new_list = []
    with codecs.open(file_name, "r", "utf-8") as file:
        list_from_file = list(file.read().split())
    for i in range(4, len(list_from_file)-1, 4):
        new_list.append([list_from_file[i], list_from_file[i+1],
                        list_from_file[i+2], list_from_file[i+3]])
    return new_list


def read_imported_file_contacts():
    view.ask_to_fill(
        "цифру названия файла\n 1- column_import.txt\n 2 - row_import.txt\n 3 и ввести название своего файла")
    check_file = int(view.get_contact_info())
    while check_file not in range(1, 4):
        view.ask_to_fill(
            "цифру названия файла\n 1 - column_import.txt\n 2 - row_import.txt\n 3 и ввести название своего файла")
        check_file = int(view.get_contact_info())
    if check_file == 1:
        readed_list = from_column_file_to_list("column_import.txt")
    elif check_file == 2:
        readed_list = from_row_file_to_list("row_import.txt")
    else:
        view.ask_to_fill("название файла")
        new_file_name = view.get_contact_info()
        view.ask_to_fill(" 1 - данные в столбце\ 2 - данные в одной строке ")
        check_file_new = int(view.get_contact_info())
        if check_file_new == 1:
            readed_list = from_column_file_to_list(new_file_name)
        elif check_file_new == 2:
            readed_list = from_row_file_to_list(new_file_name)
    return readed_list
from_row_file_to_list

def export_contacts():
    view.ask_to_fill(
        "номер экспортируемых данных:\n 1 - из файла column_import.txt\n 2 - из файла row_import.txt\n 3 - все контакты")
    check_export_file = int(view.get_contact_info())
    while check_export_file not in range(1, 4):
        view.ask_to_fill(
            "номер экспортируемых данных:\n 1 - из файла column_import.txt\n 2 - из файла row_import.txt\n 3 - все контакты")
        check_export_file = int(view.get_contact_info())
    if check_export_file == 1:
        readed_list = from_column_file_to_list("column_import.txt")
    elif check_export_file == 2:
        readed_list = from_row_file_to_list("row_import.txt")
    else:
        readed_list = from_row_file_to_list("all_contacts.txt")
    view.ask_to_fill("вид экспортируемых данных\n 1 - в столбик\ 2 - в строчку")
    check_exported_file = int(view.get_contact_info())
    while check_exported_file not in range(1, 3):
        view.ask_to_fill("вид экспортируемых данных\n 1 - в столбик\n 2 в строчку")
        check_exported_file = int(view.get_contact_info())
    if check_exported_file == 1:
        readed_list.insert(0,["Фамилия\nИмя\nНомер_телефона\nКомментарий\n"])
        add_to_all_contacts(readed_list,"exported_contacts.txt", "w","\n")
    else:
        readed_list.insert(0,["Фамилия;Имя;Номер_телефона;Комментарий"])
        add_to_all_contacts(readed_list,"exported_contacts.txt", "w",";")




