from models.authors import Author
from models.books import Book
from repository.author_repos import add_author
from repository.db_init import db_init
from repository.books_repos import add_book


def main():
    # Kreiraj autora
    first_name = input('Upiste ime autora: ')
    last_name = input('Upiste prezime autora: ')
    author = Author(first_name, last_name)
    author.id = add_author(author)

    title = input('Upiste naziv knjige: ')
    description = input('Upiste kratki opis knjige: ')
    isbn = input('Upiste ISBN knjige: ')
    price = float(input('Upiste cijenu knjige: '))
    book = Book(title, author, price, description, isbn)
    book.id = add_book(book)

    author.add_book(book)


if __name__ == '__main__':
    db_init()
    main()