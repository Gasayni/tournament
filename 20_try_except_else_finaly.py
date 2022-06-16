import os


def alpha_cnt(word, a_dct, fl=None):
    """Функция для подсчета количества букв"""

    for i_sym in word.lower():
        if i_sym.isalpha():
            fl = True
            cnt_dict['Symbol'] += 1
            if a_dct.get(i_sym):
                a_dct[i_sym] += 1
            else:
                a_dct[i_sym] = 1
    return fl


def word_cnt(line):
    """Функция для подсчета количества слов"""

    cnt_dict['Line'] += 1
    for i_word in line.split():
        if alpha_cnt(i_word, alpha_dict):
            cnt_dict['Word'] += 1


def inversion(i_dict):
    """Функция для инвертирования словаря"""

    tmp_dct = dict()
    for key, value in i_dict.items():
        if tmp_dct.get(value):
            tmp_dct[value].extend([key])
        else:
            tmp_dct[value] = [key]
    return tmp_dct


def main(alpha_dict):
    try:
        with open(os.path.join('zen.txt'), 'r') as file:
            data = file.read().split('\n')
            for i_line in data:
                word_cnt(i_line)
    except FileNotFoundError:
        print('Файл или директория не существует')
    except FileExistsError:
        print('Попытка создания файла, который уже существует.')
    except IsADirectoryError:
        print('На чтение ожидался файл, но это оказалась директория.')
    except TypeError or ValueError:
        print('Неверный тип данных и некорректное значение')
    else:
        for k, v in cnt_dict.items():
            print(f'{k}: {v}')
        alpha_dict = inversion(alpha_dict)
        print('\nRare letter:', ', '.join(alpha_dict[min(alpha_dict)]))
        # Вывод на экран букву, которая встречается в тексте наименьшее количество раз
    finally:
        print('The End!')


if __name__ == '__main__':
    alpha_dict = dict()
    cnt_dict = {'Symbol': 0, 'Word': 0, 'Line': 0}
    main(alpha_dict)
