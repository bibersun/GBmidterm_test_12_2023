from dataclass import Data

if __name__ == '__main__':
    # по умолчанию создается, если нет в наличии, файл test_data.json, но в скобках можно указать любой
    data = Data()
    while True:
        match input(
            "Введите номер\n1 - очистка всего\n2 - печать всего\n3 - добавить запись\n4 - удалить запись по "
            "id\n5 - редактировать запись по id\n6 - печать по id\n7 - сохранить в файл\n8 - печать заметок "
            "на дату\n10 - загрузка тестовых данных\n0 - сохранить в файл и выйти\n11 - выйти без сохранения\n"):
            case '1':
                data.clear_data()
            case '2':
                print(data)
            case '3':
                data.uppend_record()
            case '4':
                data.del_record(int(input("Введите Id для удаления: ")))
            case '5':
                data.update_record(int(input("Введите Id для редактирования: ")))
            case '6':
                data.print_by_id(int(input("Введите Id для печати: ")))
            case '7':
                data.save()
            case '8':
                data.print_by_date(input("Введите дату в формате yyyy/mm/dd: "))
            case '10':
                data.data = data.test_data
                data.save()
            case '0':
                data.save()
                break
            case '11':
                break
            case _:
                print('Можно вводить только числа из меню')
