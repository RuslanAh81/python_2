#  Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
#  Какие вещи взяли все три друга
#  Какие вещи уникальны, есть только у одного друга Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует Для решения используйте операции
# с множествами. Код должен расширяться на любое большее количество друзей
from collections import Counter

FRIENDS = {
    'Ваня': ('Палатка', 'Спальник', 'Горелка'),
    'Петя': ('Ложка', 'Термос', 'Чашка'),
    'Толя': ('Палатка', 'Спички', 'Соль', 'Котелок', 'Ложка', 'Нож', 'Грелка Маша'),
    'Маша': ('Палатка', 'Спальник', 'Горелка', 'Ложка', 'Термос', 'Муж')
}

all_items = Counter(item for items in FRIENDS.values() for item in items)
names = set(FRIENDS.keys())
find_friends = set()
find_items = None
items_in_friends = None

for key, value in FRIENDS.items():
    for item in value:
        if all_items.get(item, 0) == 1:
            print(f'{item} есть только у {key}')
        elif all_items.get(item, 0) == len(FRIENDS)-1:
            find_items = item
            find_friends.add(key)
        elif all_items.get(item, 0) == len(FRIENDS):
            items_in_friends = item
if find_items is not None:
    print(f'{find_items} нет у', *(names - find_friends))

if items_in_friends is not None:
    print(f'{items_in_friends} есть у всех')
