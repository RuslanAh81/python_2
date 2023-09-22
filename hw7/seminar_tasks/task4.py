# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

from random import randint, choice
import random as rnd
import string

def generate_file(extention: str,min_len: int = 6, max_len = 30, min_size: int = 256, max_size = 4096, file_count: int = 42):
    letters = string.ascii_lowercase
    for _ in range(file_count):
        name_len = rnd.randint(min_len, max_len)
        name = rnd.choices(letters, k=name_len)
        name = ''.join(name)
        file_name = name + extention
        file_size = rnd.randint(min_size, max_size)
        data = rnd.randbytes(file_size)
        with open(file_name, 'wb') as file:
            file.write(data)

    return print(file_name)


def rand_ext(ext: tuple, file_count: int = 1):
    for _ in range(file_count):
        extention = rnd.choice(ext)
        generate_file(extention, file_count=file_count)
        # print(extention)

if __name__ == '__mane__':
    rand_ext(('.txt', '.bmp', '.jpg', 'avi', 'mp3', 'doc', 'mkv'), 10)