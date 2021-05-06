"""Задача 2: Вернуть первые два символа каждого слова"""

import re

from task_1 import task_1


def task_2():
    list_first_words = task_1()
    two_char_pattern = r'..'
    # ToDo вернуть первые два символа из слова

    match_list = [
        re.search(two_char_pattern, word) for word in list_first_words]

    # [match.group() for match in match_list if match is not None]

    return [match.group() if match is not None else match
            for match in match_list]


if __name__ == '__main__':
    print(task_2())
