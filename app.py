from models.authors import Author
from models.books import Book
from repository.author_repos import add_author, get_author, get_all_authors, update_author, delete_author
from repository.db_init import db_init
from repository.books_repos import add_book, update_book, delete_book, get_book, get_all_books


def main():
    # Kreiraj autora
    # first_name = input('Upiste ime autora: ')
    # last_name = input('Upiste prezime autora: ')
    # author = Author(first_name, last_name)
    # author.id = add_author(author)

    # title = input('Upiste naziv knjige: ')
    # description = input('Upiste kratki opis knjige: ')
    # isbn = input('Upiste ISBN knjige: ')
    # price = float(input('Upiste cijenu knjige: '))
    # book = Book(title, author, price, description, isbn)
    # book.id = add_book(book)
    # new_price = float(input('Upisite novu cijenu: '))
    # book_id = int(input('Upisite id knjige: '))
    # rezultat = update_book(new_price, book_id )
    # print(rezultat)
    # books = get_all_books()
    # for book in books:
    #     print(book)
    
    # authors = get_all_authors()
    # for author in authors:
    #     print(author)

    # author.add_book(book)

    # del_author = delete_author(4)
    # print(del_author)
    authors = get_all_authors()

    for author in authors:
        print(f"Autor: {author.full_name}")
        if author.books:
            for book in author.books:
                print(f"  - {book.title}")
        else:
            print("  (nema knjiga)")



if __name__ == '__main__':
    db_init()
    main()