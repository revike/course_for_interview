"""
Создать два списка с различным количеством элементов. В первом должны
быть записаны ключи, во втором — значения. Необходимо написать функцию,
создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не
хватило ключей, необходимо отбросить.

"""
from itertools import zip_longest


def dict_in_list(list_key, list_value):
    if len(list_key) > len(list_value):
        return dict(zip_longest(list_key, list_value))
    return dict(zip(list_key, list_value))


if __name__ == '__main__':
    list_keys = ['audi', 'bmw', 'honda', 'lexus', 'kia']
    list_values = ['a7', 'x6', 'civic', 'rx']
    result = dict_in_list(list_keys, list_values)
    print(result)
