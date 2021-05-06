import json
import re


BOOK_BODY_PATTERN = re.compile(r"(?<=#### ).+?((?=####)|$)",
                               re.DOTALL)
BOOK_MD_PATTERN = re.compile(r"(?P<position>\d{1,2})\.\s\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\s+by\s+(?P<author>.+?)\s+\((?P<recommended>\d{1,3}\.\d+)%.+?!\[\]\((?P<cover_url>.+?)\)\s+\"(?P<description>.+?)\"",
                             re.DOTALL)
BOOKS_FILE = 'books.md'
BOOKS_JSON = 'books.json'


def extract_books_md_body(text):
    return [match.group() for match in BOOK_BODY_PATTERN.finditer(text)]  # ToDo map + lambda


def get_book_dict(body):
    return BOOK_MD_PATTERN.search(body).groupdict()


if __name__ == '__main__':
    with open(BOOKS_FILE) as f:
        books_body_list = extract_books_md_body(f.read())

    with open(BOOKS_JSON, 'w') as f:
        book_list = [get_book_dict(book_body) for book_body in books_body_list]  # ToDo map
        # ToDo sorted with lambda
        json.dump(book_list, f, indent=4, ensure_ascii=False)


