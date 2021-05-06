"""Задача 1: Вернуть первое слово из строки"""

import re


def task_1():
    word_list = [
        ',./ sdfsdf',
        'Ddfsdf',
        '@@##,sdfsdf',
        '123_sdfsdf',
        '123sdfsdf',
        ', s,dfsdf',
        '123, fewfew',
    ]

    word_pattern = re.compile(r"[a-zA-Z]+")
    return [word_pattern.search(str_).group() for str_ in word_list]  # map()  # ToDo


if __name__ == '__main__':
    task_1()
