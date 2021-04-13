"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл. Если файл с таким
именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и
числовой информацией. Для создания списков использовать генераторы.
Применить к спискам функцию zip(). Результат выполнения этой функции
должен быть обработан и записан в файл таким образом, чтобы каждая строка
файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой
построчный вывод содержимого. Вся программа должна запускаться по
вызову первой функции.
"""
import string
from os.path import exists
from random import choice, randint


def create_file(file_write):
    list_str = [i for i in ''.join(choice(string.ascii_lowercase)
                                   for _ in range(randint(10, 10)))]
    list_int = [j for j in range(1, 11)]

    list_zip = dict(zip(list_str, list_int))
    if exists(file_write):
        with open(file_write, 'w', encoding='utf8') as obj:
            for k, v in list_zip.items():
                line = f'{k} {v}\n'
                obj.write(line)
        return read_file(file_write)
    obj = open(file, 'w', encoding='utf8')
    obj.close()
    return create_file(file_write)


def read_file(file_read):
    with open(file_read, encoding='utf8') as obj:
        res = obj.read()
        return res


if __name__ == '__main__':
    file = 'file.txt'
    result = create_file(file)
    print(result)
