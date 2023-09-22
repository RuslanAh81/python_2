# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def mult_func():
    data1 = []
    with open('text_seminar.txt', 'r', encoding='utf-8') as file1:
        data1 = file1.readlines()

    data2 = [8]
    with open('name_seminar.txt', 'r', encoding='utf-8') as file2:
        data2 = file2.readlines()

    with open('task3_mult.txt', 'a+', encoding='utf-8') as file3:
        data3 = []
        max_size = max(len(data1), len(data2))
        min_size = min(len(data1), len(data2))

        for i in range(max_size):
            a, b = data1[i % min_size].split('|')
            mult =int(a) * float(b)
            if mult < 0:
                data3.append(f'{data2[i % min_size].lower().strip()} | {abs(mult)}')
            else:
                data3.append(f'{data2[i % min_size].upper().strip()} | {int(mult)}')

        # print(data3)
        file3.write('\n'.join((data3)))


if __name__ == '__main__':
    mult_func()