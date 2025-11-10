from __future__ import annotations


class Book:
    def __init__(self, title: str, author: 'Author', price: float, description: str = '', isbn: str = ''):
        self.id: int = 0
        self.title: str = title
        self.price: float = price
        self.author: 'Author' = author
        self.description:str = description
        self.isbn:str = isbn

    def __str__(self):
        return f'{self.title} ({self.author._full_name()})'