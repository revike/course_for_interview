"""
 Усовершенствовать первую функцию из предыдущего примера.
 Необходимо во втором списке часть строковых значений заменить на значения
 типа example345 (строка+число). Далее — усовершенствовать вторую функцию из
 предыдущего примера (функцию извлечения данных). Дополнительно реализовать
 поиск определенных подстрок в файле по следующим условиям: вывод первого
 вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок
 на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих
 пробелы только в начале и конце — например, example345.
"""
import re
import string
from os.path import exists
from random import choice, randint, randrange


def create_file(file_write):
    list_str = [f'{i}{randrange(1, 10)}' for i in
                ''.join(choice(string.ascii_lowercase)
                        for _ in range(randint(10, 10)))]
    list_int = [j for j in range(1, 11)]

    list_zip = dict(zip(list_str, list_int))
    if exists(file_write):
        with open(file_write, 'w', encoding='utf8') as obj:
            for k, v in list_zip.items():
                line = f'{k} {v}\n'
                obj.write(line)
        return read_file(file_write)
    open(file, 'w', encoding='utf8')
    return create_file(file_write)


def read_file(file_read):
    with open(file_read, encoding='utf8') as obj:
        res = obj.read()
        first_occ = re.search(r'[a-l]\d', res).group(0)
        all_occ = re.findall(r'[a-l]\d', res)
        res_all_occ = re.sub(r'[a-l]\d', 'example345', res)
        out = re.findall(r'\w+\d{3}\s', res_all_occ)
        res_return = f'first_occ - {first_occ}\n' \
                     f'all_occ - {all_occ}\n' \
                     f'out - {out}'
        return res_return


if __name__ == '__main__':
    file = 'file.txt'
    result = create_file(file)
    print(result)
