from datdbase import *

def input_num():
    ask = int(input('Выберите действие: \n 1 - Записать нового абонента\n 2 - Найти абонента\n '
                    '3 - Найти и изменить запись\n 4 - Найти и удалить запись\n 5 - Удалить все\n '
                    '6 - Отсортировать по параметру\n 7 - Показать весь список контактов\n'))
    return ask

def input_name():
    #id = input('Введите id: ')
    id = '1'
    with open("input.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        lst.sort(key= lambda x: int(x.split(',')[0]))
        for row in lst:
            if row.split(',')[0] == id:
                id = str(int(id) + 1) 
    name = input('Введите имя: ')
    surname = input('Ввелите фамилию: ')
    tel = input('Введите номер телефона: ')
    res = id + "," + name + "," + surname + ',' + tel + '\n' 
    return res

def input_search_char():
    search_char = int(input('Выберите параметр поиска: \n 1 - id \n 2 - имя \n 3 - фамилия \n'))
    return search_char

def input_char():
    char = input("Введите параметр:\n")
    return char

def sort_char():
    ask = int(input('Выберите параметр сортировки: \n 1 - id \n 2 - имя \n 3 - фамилия \n'))
    return ask