import sqlite3

from constants import DB_PATH
from models.books import Book
from models.authors import Author


sql_create_book = '''
INSERT INTO book (title, description, isbn, price, author_id)
VALUES (?, ?, ?, ?, ?)
'''
sql_get_book = '''
SELECT * FROM book
WHERE id = ?
'''
sql_delete_book = '''
DELETE FROM book
WHERE id = ?
'''

sql_update_book ='''
    UPDATE book
    SET price = ?
    WHERE id = ?
'''
sql_get_all_books = '''
    SELECT first_name, last_name FROM book
    WHERE id = ?
    ROW = ?
'''

def add_book(book: Book) -> int:
    if isinstance(book, Book):
        params = (book.title, book.description, book.isbn, book.price, book.author.id)
    else:
        return

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_book, params)
            return cursor.lastrowid
    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def get_book(id) -> Book:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_get_book, (id,))
            row = cursor.fetchone()

            if row:
                cursor.execute('SELECT first_name, last_name FROM author WHERE id = ?', (row[5],))
                author_row = cursor.fetchone()
                author = Author(*author_row) if author_row else None
                book = Book(
                    title = row[1],
                    author = author,
                    price = row[4],
                    description = row[2],
                    isbn=row[3]
                )
                book.id = row[0]
                return book
            return None
            # medu korak dohvatiti autora iz baze i napraviti objekt Author
            # kada su svi podaci spremni napraviti objekt Book i vratiit ga pomocu return

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


def get_all_books() -> list[Book]:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM book')
            rows = cursor.fetchall()
            books = []
            for row in rows:
                if row:
                    cursor.execute('SELECT first_name, last_name FROM author WHERE id = ?', (row[5],))
                    author_row = cursor.fetchone()
                    author = Author(*author_row) if author_row else None
                    book = Book(
                        title = row[1],
                        author = author,
                        price = row[4],
                        description=row[2],
                        isbn=row[3]
                    )
                    book.id = row[0]
                    books.append(book)
            return books
                
    except Exception as ex:
        print (f'Greska {ex}')
        return []

def delete_book(id: int) -> str:
    # 1. dohvatiti knjigu iz baze koja ima dobiveni ID
    book_from_db = get_book(id)

    # 2. ako postoji knjiga u bazi izbrisi je i vrati poruku OK
    if book_from_db is not None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_delete_book, (id,))
                conn.commit()
                return 'OK'
        except Exception as ex:
            print(f'Dogodila se greska {ex}.')

    # ako ne postoji vratiti poruku da nema takve knjige u bazi
    else:
        return f'Ne postoji trazena knjiga u bazi!'
    

def update_book(new_price: float, book_id: int) -> str:
    book_from_db = get_book(book_id)

    if book_from_db is not None:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_update_book, (new_price, book_id))
                conn.commit()
                return 'Azurirano'
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
        
    else:
        return f'Ne postoji trazena knjiga'
    
def get_book_by_author_id(author_id: int) -> list[Book]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, author_id FROM book WHERE author_id = ?', (author_id,))
        rows = cursor.fetchall()

        books = []
        for row in rows:
            book = Book(title=row[1], author_id=row[5])
            book.id = row[0]
            books.append(book)
        return books