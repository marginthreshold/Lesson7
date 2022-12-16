import controller as c
import view as v


check_file = 1  

while check_file in range(1, 6):
    v.ask_to_fill(
        "пункт меню:\n 1 - Добавление нового контакта вручную.\n 2 - Добавление\
 контактов через импортируемый файл\n 3 - Экспорт контактов в файл\n 4 - Просмотр списка контактов\n 5 - Выход из меню (")
    check_file = int(v.get_contact_info())
    if check_file == 1:
        c.add_to_all_contacts(c.create_contact(), "all_contacts.txt", "a", ";")
    elif check_file == 2:
        c.add_to_all_contacts(c.read_imported_file_contacts(),
                              "all_contacts.txt", "a", ";")
    elif check_file == 3:
        c.export_contacts()
    elif check_file == 4:
        v.print_list(c.from_row_file_to_list("all_contacts.txt"))
    else:
        break
