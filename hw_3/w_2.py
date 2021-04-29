"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.

"""
from math import modf


def number_input(num):
    try:
        if isinstance(int(num), int):
            return f'Число {num} целое!'
    except ValueError:
        try:
            if isinstance(float(num), float):
                first_num = modf(float(num))[1]
                second_num = float(num.split('.')[1])
                return f'Число {num} дробное! - {first_num == second_num}'
        except ValueError:
            num = input('\nНеобходимо ввести число: ')
            return number_input(num)


if __name__ == '__main__':
    number = input('Введите число: ')
    result = number_input(number)
    print(result)
