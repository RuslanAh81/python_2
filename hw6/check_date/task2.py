# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse
from check_exists import date_funct

parser = argparse.ArgumentParser(description='Проверка даты')
parser.add_argument('date', type=str, help='Дата в формате ДД.ММ.ГГГГ')

args = parser.parse_args()

if date_funct(args.date):
    print(f'Дата{args.date} существует')
else:
    print(f'Дата{args.date} не существует')