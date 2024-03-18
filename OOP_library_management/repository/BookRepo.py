
class BookRepo:
    def __init__(self):
        self._books = []

    def get_books_by_string_attribute(self, value, atr):
        return [book for book in self._books if value.lower() in getattr(book, atr).lower()]

    def add_book(self, book):
        self._books.append(book)

    def get_books(self):
        return self._books

    def get_book_by_isbn(self, isbn):
        for book in self.get_books():
            if book.isbn.lower() == isbn.lower():
                return book
        return None

