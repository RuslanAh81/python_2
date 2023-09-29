import os
import json
import csv
import random as rnd
from typing import Callable


def csv_dekor(func: Callable):
    result_dict = {}

    def wrapper(*args):
        if len(args) == 1:
            if os.path.isfile(*args):
                with open(*args, 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file, dialect='excel')
                    for line in csv_reader:
                        a, b, c = (list(map(int, line)))
                        if a:
                            result_dict[f'Значения: {a = }, {b = }, {c = }'] = func(a, b, c)
        elif len(args) == 3:
            if args[0]:
                result_dict[f'Значения:a= {args[0]}, b={args[1]}, c={args[2]}'] = func(*args)
        return result_dict

    return wrapper


def json_decor(filename: str = 'result.json'):
    def decor(func: Callable):
        def wrapper(*args):
            result = func(*args)
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(result, file, indent=4, ensure_ascii=False)
            return result

        return wrapper

    return decor
@json_decor()
@csv_dekor
def find_roots(a, b, c):
    discr = b**2 - 4 * a * c
    if discr < 0:
        return 'Нет корней'
    elif discr == 0:
        return round((-b) / 2 * a, 3)
    return round((-b - discr ** 0.5) / 2 * a, 3), round((-b + discr ** 0.5) / 2 * a, 3)


def gener_rand_csv(path):
    csv_data = [(rnd.randint(0, 10) for _ in range(3)) for _ in range(100)]
    with open(path, 'w', newline='') as file:
        csv_writer = csv.writer(file, dialect='excel')
        csv_writer.writerows(csv_data)


if __name__ == '__main__':
    gener_rand_csv('rand_list.csv')
    find_roots(10, 10, 50)
    print(find_roots('rand_list.csv'))
