# напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки : "Число является простым, если дклится нацело только на единицу и на себя". Сделайте ограничение на
# ввод отрицательных чисел и чисел больше 100 тысяч.

flag = True
while flag:
    a = int(input("Введите положительное число не больше 100000: "))
    if a < 0 or a > 100000:
        print("Вы должны ввести положительное число и число меньше 100000")
        continue
    for i in range(2, a // 2 +1):
        if a % i == 0:
            print("Число не является простым")
            flag = False
            break
    else:
        print("Число является простым")
        flag = False