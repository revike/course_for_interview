"""
1. Написать программу, которая будет содержать функцию для получения имени
файла из полного пути до него. При вызове функции в качестве аргумента должно
передаваться имя файла с расширением. В функции необходимо реализовать поиск
полного пути по имени файла, а затем «выделение» из этого пути имени
файла (без расширения).
"""
from os import getcwd
from os.path import join, exists


def get_name_file(file):
    paths = getcwd()
    res = join(paths, file)
    if exists(res):
        return res.split('\\')[-1].split('.')[0]
    return 'not file'


if __name__ == '__main__':
    print(get_name_file('1.py'))
