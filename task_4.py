import re


def task_4():
    date_str = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
    date_pattern = re.compile(
        r"(?P<day>\d\d)-(?P<month>\d\d)-(?P<year>\d\d\d\d)")

    for match in date_pattern.finditer(date_str):
        print(match['day'])


if __name__ == '__main__':
    task_4()
