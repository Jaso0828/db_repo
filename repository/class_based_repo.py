import sqlite3
from typing import List, Optional


# ---------- MODELS ----------
class Author:
    def __init__(self, id: int = None, name: str = ""):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}')"


class Book:
    def __init__(self, id: int = None, title: str = "", author_id: int = None):
        self.id = id
        self.title = title
        self.author_id = author_id

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author_id={self.author_id})"


# ---------- REPOSITORY BASE ----------

class Repo:
    def __init__(self, db_path: str = "data_store/library.db"):
        self.db_path = db_path
        self._create_tables()
        # Opcionalno dodati self._db_seed() metodu
        # koja ce napuniti bazi inicijalnim podacima
        # self._db_seed()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_tables(self):
        """Create tables if they don’t exist."""
        with self._get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE
                )
            """)
            conn.commit()

    # ---------- CRUD for Author ----------

    def add_author(self, author: Author) -> int:
        with self._get_connection() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO authors (name) VALUES (?)", (author.name,))
            conn.commit()
            return cur.lastrowid

    def get_author(self, author_id: int) -> Optional[Author]:
        with self._get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
            row = cur.fetchone()
            return Author(row["id"], row["name"]) if row else None

    def list_authors(self) -> List[Author]:
        with self._get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM authors")
            return [Author(row["id"], row["name"]) for row in cur.fetchall()]

    def update_author(self, author: Author):
        with self._get_connection() as conn:
            conn.execute("UPDATE authors SET name = ? WHERE id = ?", (author.name, author.id))
            conn.commit()

    def delete_author(self, author_id: int):
        with self._get_connection() as conn:
            conn.execute("DELETE FROM authors WHERE id = ?", (author_id,))
            conn.commit()

    # ---------- CRUD for Book ----------

    def add_book(self, book: Book) -> int:
        with self._get_connection() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO books (title, author_id) VALUES (?, ?)",
                        (book.title, book.author_id))
            conn.commit()
            return cur.lastrowid

    def get_book(self, book_id: int) -> Optional[Book]:
        with self._get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE id = ?", (book_id,))
            row = cur.fetchone()
            return Book(row["id"], row["title"], row["author_id"]) if row else None

    def list_books(self, author_id: Optional[int] = None) -> List[Book]:
        with self._get_connection() as conn:
            cur = conn.cursor()
            if author_id:
                cur.execute("SELECT * FROM books WHERE author_id = ?", (author_id,))
            else:
                cur.execute("SELECT * FROM books")
            return [Book(row["id"], row["title"], row["author_id"]) for row in cur.fetchall()]

    def update_book(self, book: Book):
        with self._get_connection() as conn:
            conn.execute("UPDATE books SET title = ?, author_id = ? WHERE id = ?",
                         (book.title, book.author_id, book.id))
            conn.commit()

    def delete_book(self, book_id: int):
        with self._get_connection() as conn:
            conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()