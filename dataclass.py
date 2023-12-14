import json
from datetime import datetime


class Data:
    # JSON_file = "test_data.json"

    # test_data = []
    test_data = [{'id': 15, 'subject': "Проба пера 1", "content": "Проба пера 1 длинная", "date": '2023/12/10 17:26'},
                 {'id': 16, 'subject': "Проба пера 2", "content": "Проба пера 2 длинная", "date": '2023/12/10 16:06'},
                 {'id': 17, 'subject': "Проба пера 3", "content": "Проба пера 3 длинная", "date": '2023/12/10 15:16'},
                 {'id': 18, 'subject': "Проба пера 4", "content": "Проба пера 4 длинная", "date": '2023/12/11 14:26'},
                 {'id': 19, 'subject': "Проба пера 5", "content": "Проба пера 5 длинная", "date": '2023/12/13 13:36'},
                 {'id': 20, 'subject': "Проба пера 6", "content": "Проба пера 6 длинная", "date": '2023/12/13 12:46'},
                 {'id': 21, 'subject': "Проба пера 7", "content": "Проба пера 7 длинная", "date": '2023/11/15 11:56'},
                 {'id': 22, 'subject': "Проба пера 8", "content": "Проба пера 8 длинная", "date": '2023/11/18 10:06'},
                 {'id': 23, 'subject': "Проба пера 9", "content": "Проба пера 9 длинная", "date": '2023/12/3 11:36'},
                 {'id': 24, 'subject': "Проба пера 10", "content": "Проба пера 10 длинная", "date": '2023/12/3 12:26'},
                 {'id': 25, 'subject': "Проба пера 11", "content": "Проба пера 11 длинная", "date": '2023/12/7 13:56'},
                 {'id': 26, 'subject': "Проба пера 12", "content": "Проба пера 12 длинная", "date": '2023/12/7 14:22'},
                 {'id': 27, 'subject': "Проба пера 13", "content": "Проба пера 13 длинная", "date": '2023/12/5 15:24'},
                 {'id': 28, 'subject': "Проба пера 14", "content": "Проба пера 14 длинная", "date": '2023/12/5 16:37'},
                 {'id': 29, 'subject': "Проба пера 15", "content": "Проба пера 15 длинная", "date": '2023/11/23 17:11'},
                 {'id': 30, 'subject': "Проба пера 16", "content": "Проба пера 16 длинная", "date": '2023/11/24 18:16'},
                 {'id': 126, 'subject': "Проба пера 17", "content": "Проба пера 17 длинная",
                  "date": '2023/11/17 19:21'},
                 {'id': 127, 'subject': "Проба пера 18", "content": "Проба пера 18 длинная",
                  "date": '2023/11/13 01:33'},
                 {'id': 128, 'subject': "Проба пера 19", "content": "Проба пера 19 длинная",
                  "date": '2023/11/10 01:44'},
                 {'id': 129, 'subject': "Проба пера 20", "content": "Проба пера 20 длинная",
                  "date": '2023/11/13 02:55'},
                 {'id': 130, 'subject': "Проба пера 21", "content": "Проба пера 21 длинная",
                  "date": '2023/12/13 03:08'}]

    # data = []

    def __init__(self, JSON_file="test_data.json"):
        self.JSON_file = JSON_file
        try:
            with open(JSON_file, encoding='utf-8') as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            new_file = open(JSON_file, 'w', encoding='utf-8')
            new_file.write('[]')
            new_file.close()
            self.data = []

    # def __del__(self):
    #     self.save()

    def __str__(self):
        if len(self.data) > 0:
            s = ''
            for item in self.data:
                s += (str(item.get('id')) + "\t" + item.get('subject') + '\t' + item.get('content') + "\t" + item.get(
                    'date') + "\t\n")
        else:
            s = 'Нет данных\n'
        return s

    def print_by_id(self, item):
        try:
            id_to_print = int(self.get_idx_by_id(item))
            print(
                str(self.data[id_to_print].get('id')) + "\t" + self.data[id_to_print].get('subject') + '\t' + self.data[
                    id_to_print].get('content') + "\t" + self.data[id_to_print].get('date') + "\t")
        except TypeError:
            print("Не удалось распечатать запись.")

    def uppend_record(self):
        id_next = max([x["id"] for x in self.data]) + 1 if len(self.data) > 0 else 1
        subject = input("Введите тему: ")
        content = input("Ведите текст заметки: ")
        ddate = datetime.now().strftime("%Y/%m/%d %H:%M")
        self.data.append({'id': id_next, 'subject': subject, 'content': content, 'date': ddate})

    def del_record(self, key):
        try:
            id_to_delete = int(self.get_idx_by_id(key))
            del self.data[id_to_delete]
            print("Запись удалена")
        except TypeError:
            print("Не удалось удалить запись.")

    def get_idx_by_id(self, ids):
        try:
            return {x[1]["id"]: x[0] for x in zip([x for x in range(len(self.data))], self.data)}[ids]
        except KeyError as e:
            print(f'Нет такого id = {ids}')

    def update_record(self, key):
        try:
            id_to_set = int(self.get_idx_by_id(key))
            self.data[id_to_set]["subject"] = input("Введите новую тему")
            self.data[id_to_set]["content"] = input("Введите новое тело заметки: ")
            self.data[id_to_set]["date"] = datetime.now().strftime("%Y/%m/%d %H:%M")
        except TypeError:
            print('Не удалось отредактировать запись.')

    def save(self):
        with open(self.JSON_file, "w", encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False)
            # json_file.close()

    def print_by_date(self, date):
        try:
            date = datetime.strptime(date, "%Y/%m/%d").date()
            s = list(filter(lambda x: datetime.strptime(x["date"], "%Y/%m/%d %H:%M").date() == date, self.data))
            if len(s) > 0:
                st = ''
                for item in s:
                    st += (str(item.get('id')) + "\t" + item.get('subject') + '\t' + item.get('content') + "\t" + item.get(
                        'date') + "\t\n")
            else:
                st = 'Нет данных\n'
            print(st)
        except ValueError:
            print("Неправильный формат даты, требуется yyyy/mm/dd")

    def clear_data(self):
        print('Данные очищены')
        self.data.clear()
