# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

num = randint(0, 1000)
count = 0
print(" Я загадал число от 0 до 1000, Попробуй его угадать )")
flag = True
while flag and count !=10:
    print(f' У вас {10-count} попыток')
    count += 1
    a = int(input("Введите свое число :"))
    if a < num:
        print(" Больше")
    elif a > num:
        print("Меньше")
    elif a == num:
        print("Угадал!!")
flag = False
print(f'Я загадал {num}')



