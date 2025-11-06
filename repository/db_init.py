import sqlite3

from constants import DB_PATH


sql_create_table_author = '''
CREATE TABLE IF NOT EXISTS author
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
'''
sql_create_table_book = '''
CREATE TABLE IF NOT EXISTS book
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NULL,
    isbn TEXT NULL,
    price REAL NOT NULL,
    author_id INTEGER NOT NULL,

    FOREIGN KEY (author_id)
        REFERENCES author (id)
);
'''


def db_init():
    try:
        # with automatski zatvara konekciju (conn.close()) i radi commit (conn.commit())
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_table_author)
            cursor.execute(sql_create_table_book)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')