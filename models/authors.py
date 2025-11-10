from __future__ import annotations


class Author:
    def __init__(self, first_name: str, last_name: str):
        self.id: int = 0
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self._full_name()
        self.books = []
    

    def _full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self._full_name()

    def add_book(self, book: 'Book'):
        self.books.append(book)

    def load_books(self):
        from repository.books_repos import get_book_by_author_id
        self.books = get_book_by_author_id(self.id)
