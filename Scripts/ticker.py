# — coding: utf-8 —

# ticker.py -- позволяет вывести текст в терминале в виде бегущей строки
# Пример запуска: python ticker.py "Hello World"

import datetime
from sys import argv
from time import sleep


def syntax_info():
    """ Вывод информации о синтаксисе программы """
    return "Синтаксис: python ticker.py [string:str] [max length:int] [file name:str]"


def file_generation(filename: str, maxlen: int, string: str):
    """ Генерирует файл для будущей бегущей строки """
    stringlen = len(string)
    # Создание начальной (первой) строки
    main_line = " " * (stringlen + maxlen) + string
    out_list = []  # Здесь будут храниться строки

    # Генерируем начальный (не урезанный) блок
    for i in range(len(main_line) - stringlen + 1):
        out_line = main_line[i:] + " " * i
        out_list.append(out_line)

    # Урезаем и записываем в файл
    file = open(filename, "w")
    for i in range(len(out_list)):
        out_line = out_list[i][stringlen:stringlen + maxlen]
        file.write(out_line + "\n")
    file.close()


if __name__ == "__main__":
    # СОЗДАЕМ ПЕРЕМЕННУЮ FILENAME: Название файла
    try:
        FILENAME = argv[3]
    except IndexError:
        now = datetime.datetime.now()
        FILENAME = f"{now.hour}{now.minute}{now.second}{now.microsecond}.gen.t"

    # СОЗДАЕМ ПЕРЕМЕННУЮ STRING: Строка для вывода
    try:
        STRING = argv[1]
    except IndexError:
        print(f"ERROR: Первым аргументом должна передоваться строка\n{syntax_info()}")
        exit()

    # СОЗДАЕМ ПЕРЕМЕННУЮ MAXLEN: Максимальное кол-во символов
    try:
        try:
            MAXLEN = int(argv[2])
        except ValueError:
            print(f"ERROR: Тип объекта MAXLEN должен быть int\n{syntax_info()}")
            exit()
    except IndexError:
        MAXLEN = 25

file_generation(FILENAME, MAXLEN, STRING)
