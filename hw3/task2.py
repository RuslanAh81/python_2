# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

first_list = [2, 47, 0, 54, 0, 73, 47, 0, 38, 2]
second_list = []

for i in set(first_list):
    if first_list.count(i) != 1:
        second_list.append(i)

print(second_list)
