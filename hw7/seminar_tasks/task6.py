# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import os
import random as rnd
import string


def generate_file(extention: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
                  file_count: int = 42, direct: str = ''):
    letters = string.ascii_lowercase

    if direct:
        if not os.path.isdir(direct):
            os.mkdir(direct)

    for _ in range(file_count):
        name_len = rnd.randint(min_len, max_len)
        name = rnd.choices(letters, k=name_len)
        name = ''.join(name)

        if os.path.isfile(os.path.join(direct, name + extention)):
            c = 1
            while os.path.isfile(os.path.join(direct, name + f'_{c}' + extention)):
                c += 1
            file_name = name + f'_{c}' + extention
        else:
            file_name = ''.join(name) + extention

        file_size = rnd.randint(min_size, max_size)
        data = rnd.randbytes(file_size)
        with open(os.path.join(direct, file_name), 'wb') as file:
            file.write(data)

    # return print(file_name)


def rand_ext(ext: tuple, file_count: int = 1, direct: str = ''):
    for _ in range(file_count):
        extention = rnd.choice(ext)
        generate_file(extention, direct=direct, file_count=file_count)
        print(extention, file_count)

# if __name__ == '__main__':
rand_ext(('.txt', '.bmp', '.jpg', '.avi', '.mp3', '.doc', '.mkv'), 10, 'mix')