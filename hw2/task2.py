# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего
# кода используйте модуль fractions.
# НЕТ ПРОВЕРКИ НА ПРАВИЛЬНОСТЬ ВВОДА, НЕТ ВООБЩЕ НИКАКОЙ ПРОВЕРКИ

from fractions import Fraction
from math import gcd

first_str = list(map(int, input('Введите первую строку вида a/b: ').split('/')))
second_str = list(map(int, input('Введите вторую строку вида a/b:').split('/')))

numerator_summ = first_str[0] * second_str[1] + first_str[1] * second_str[0]
denominator_summ = first_str[1] * second_str[1]
summ_frac = [numerator_summ // gcd(numerator_summ, denominator_summ), denominator_summ // gcd(numerator_summ, denominator_summ)]

numerator_multy = first_str[0] * second_str[0]
denominator_multy = first_str[1] * second_str[1]
multy_frac = [numerator_multy // gcd(numerator_multy, denominator_multy), denominator_multy // gcd(numerator_multy, denominator_multy)]

result_1 = f'{summ_frac[0]}/{summ_frac[1]}' if summ_frac[1] != 1 else summ_frac[0]
result_2 = f'{multy_frac[0]}/{multy_frac[1]}' if multy_frac[1] != 1 else multy_frac[0]

print(f'Результат Сумма : {result_1}; Произведение: {result_2}')

frac_1 = Fraction(first_str[0], first_str[1])
frac_2 = Fraction(second_str[0], second_str[1])

print(f'Проверка Сумма: {frac_1 + frac_2}; Произведение :{frac_1 * frac_2}')