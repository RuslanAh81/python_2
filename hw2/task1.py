# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

number = int(input('Введите число :'))
#base = int(input('ВВедите систему счисления :'))
base = 16
hex_string = '0123456789abcdef'

original_number = number
result_number = ''
while number:
    result_number = hex_string[number % base] + result_number
    number //= base
print(f'число {original_number} в {base}-ичной системе счисления будет: {result_number}')
print(hex(original_number))

