import sqlite3

from constants import DB_PATH
from models.authors import Author


sql_create_author = '''
INSERT INTO author (first_name, last_name)
VALUES (?, ?)
'''
sql_get_author_by_name = '''
SELECT * FROM author
WHERE first_name LIKE '?'
'''


def add_author(author: Author) -> int:
    if isinstance(author, Author):
        params = (author.first_name, author.last_name)
    else:
        return

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_author, params)
            return cursor.lastrowid
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')