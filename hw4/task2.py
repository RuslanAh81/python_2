# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хэшируется,
# используйте его строковое представление.

def my_func(**kwargs):
    my_dict = {}
    for key, arg in kwargs.items():
        if not getattr(arg, '__hash__', None):
            arg = str(arg)
        my_dict[arg] = key
    return my_dict


print(my_func(a=1, b='be', c=['ce', 'de'], d={1, 2}))