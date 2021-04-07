"""
Написать функцию (несколько функций), реализующую вывод таблицы умножения
размерностью AｘB. Первый и второй множитель должны задаваться в виде
аргументов функции.
"""


def table_logic_1(a, b):
    x, y = 1, 1

    while x <= a:
        output = f'{x} X {y} = {x * y}'
        if y > b:
            y = 1
            x += 1
            if x > a:
                break
            print('\n')
            continue
        y += 1
        print(output)


def multiplication_table_1(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > 0 and b > 0:
            return table_logic_1(a, b)
        return 'A и B должны быть целыми положительными числами'
    return 'A и B должны быть целыми числами!'


# =================================================


def table_logic_2(a, b, x=1, y=1, output=None):
    while x <= a:
        output = f'{x} X {y} = {x * y}'
        if y > b:
            y = 1
            x += 1
            print('\n')
            if x > a:
                return
            return table_logic_2(a, b, x, y, output)
        y += 1
        print(output)
        return table_logic_2(a, b, x, y, output)


def multiplication_table_2(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > 0 and b > 0:
            return table_logic_2(a, b)
        return 'A и B должны быть целыми положительными числами'
    return 'A и B должны быть целыми числами!'


result_1 = multiplication_table_1(5, 5)
print(f'\n{"=" * 10}\n')
result_2 = multiplication_table_2(3, 3)
