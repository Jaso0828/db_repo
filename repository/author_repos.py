import sqlite3

from constants import DB_PATH
from models.authors import Author
from repository.books_repos import get_book_by_author_id


sql_create_author = '''
INSERT INTO author (first_name, last_name)
VALUES (?, ?)
'''

sql_get_all_authors = '''
    SELECT * FROM author
'''

sql_get_author = '''
    SELECT * FROM author
    WHERE id = ?
'''

sql_update_author = '''
    UPDATE author
    SET = firts_name = ?, last_name = ?
    WHERE id = ?
'''

sql_delete_author = '''
    DELETE FROM author
    WHERE id = ?
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


def get_author(id) -> Author:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_get_author, (id,))
            row = cursor.fetchone()

            if row:
                author = Author(
                    first_name = row[1],
                    last_name = row[2]
                )
                author.id = row[0]
                return author
            return None
    except Exception as ex:
        return f'Greska {ex}'
    

def get_all_authors() -> list[Author]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_get_all_authors)
        rows = cursor.fetchall()
        authors = []

        for row in rows:
            if row:
                author = Author(
                    first_name=row[1],
                    last_name=row[2]
                )
                author.id = row[0]
                author.books = get_book_by_author_id(author.id)
                authors.append(author)
        return authors


def update_author(id: int, first_name: str, last_name: str) -> Author:
    authors_from_db = get_author(id)

    if authors_from_db is not None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_update_author, (id, first_name, last_name))
                conn.commit()
                return f'Autor {id} azuriran'
        except Exception as ex:
            return f'Greska {ex}'
    else:
        return f'Ne postoji autor'
    

def delete_author(id: int) -> str:
    author_from_db = get_author(id)

    if author_from_db is not None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_delete_author, (id,))
                conn.commit
                return f'Autor pod ID {id} je izbrisan'
        except Exception as ex:
            return f'Dogodila se greska {ex}'    
    else:
        return f'Autor ne postoji'

