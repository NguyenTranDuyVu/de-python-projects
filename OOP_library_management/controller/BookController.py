from repository import BookRepo


class BookController:
    @classmethod
    def get_books_by_string_attribute(cls, book_repo, message, attribute):
        content = input(message)
        return book_repo.get_books_by_string_attribute(content, attribute)

    @classmethod
    def borrow_book(cls, catalog, isbn):
        for book in catalog.get_books():
            if book.isbn == isbn:
                return book.borrow()
        print(f'Book cannot be found')

    @classmethod
    def get_book_by_isbn(cls,book_repo, isbn):
        return book_repo.get_book_by_isbn(isbn)

