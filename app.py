# from models.authors import Author
# from models.books import Book
# from repositories.author_repos import add_author
# from repositories.db_init import db_init
# from repositories.book_repos import add_book
from repository.class_based_repo import Author, Book, Repo


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

    # author.add_book(book)
    pass


if __name__ == '__main__':
    # db_init()
    # main()



    repo = Repo()

    # Create Author and Book
    author_id = repo.add_author(Author(name="George Orwell"))
    repo.add_book(Book(title="1984", author_id=author_id))
    repo.add_book(Book(title="Animal Farm", author_id=author_id))

    # List authors and books
    print("Authors:", repo.list_authors())
    print("Books:", repo.list_books(author_id))