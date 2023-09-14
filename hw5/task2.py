# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла

import os
from typing import Any

my_str_ = 'C:/Users/Ruslan/Desktop/Screenshot_1.jpg'


def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)


# def parse_path_2(path: str) -> tuple[str, Any]:
#     return os.path.split(path)[0], *os.path.split(path)[1].split('.')


# print(parse_path_2(my_str_))
print(parse_path(input('Введите путь к файлу: ')))
