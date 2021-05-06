import re


def task_3():
    emails_str = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
    domain_pattern = re.compile(r'@(\w+\.\w+)')
    list_domains = domain_pattern.findall(emails_str)

    return list_domains


if __name__ == '__main__':
    print(task_3())
