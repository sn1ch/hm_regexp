from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("data/phonebook_raw.csv", encoding='cp1251') as uniting_dict:
    rows = csv.reader(uniting_dict, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
correct_FIO_contacts_list = []
for contact in contacts_list:
    FIO = re.split("\s+", contact[0] + " " + contact[1] + " " + contact[2])
    if "" in FIO:
        FIO.remove("")
    FIO = tuple(FIO)
    correct_FIO_contacts_list.append(list(FIO) + contact[3:])

correct_FIO_contacts_list[8].append(correct_FIO_contacts_list[8][5])
correct_FIO_contacts_list[8][5] = ""

uniting_dict = {}
for contact in correct_FIO_contacts_list:
    if contact[0] not in uniting_dict.keys():
        uniting_dict.setdefault(contact[0], contact[1:])
    else:
        for _ in range(6):
            if uniting_dict[contact[0]][_] != "":
                continue
            else:
                uniting_dict[contact[0]][_] = contact[_ + 1]

last_contacts_list = []
for i in uniting_dict.values():
    last_contacts_list.append(i)

count = 0
for lastname in uniting_dict.keys():
    if count != len(last_contacts_list):
        last_contacts_list[count].insert(0, lastname)
    count += 1
pprint(last_contacts_list)

pattern_phone = \
    '((8|\+7)[\- ]?)?(\()?(\d{3})?(\))?[\- ]?(\d{3})?[\- ]?(\d{2})?[\- ]?(\d{2})(\s*)(\()?(доб.)*(\s)?(\d{4})?(\))?'
for contact in last_contacts_list:
    phone = contact[5]
    new_phone_format = re.sub(pattern_phone, r"+7(\4)\6-\7-\8 \11\13", phone)
    contact[5] = new_phone_format

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("data/phonebook.csv", "w", encoding='UTF8', newline='') as uniting_dict:
    datawriter = csv.writer(uniting_dict, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(last_contacts_list)
