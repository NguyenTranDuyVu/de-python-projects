class Book:
    def __init__(self, isbn, title, authors, year, publisher, status='Available'):
        self.title = title
        self.isbn = isbn
        self.authors = authors
        self.year = year
        self.publisher = publisher
        self.status = status

    def __repr__(self):
        return f'{type(self).__name__}({self.isbn}, {self.title}, {self.authors}, {self.year}, {self.publisher}, {self.status})'

    def borrow(self):
        if self.status == 'Available':
            self.status = 'Loaned'
            print(f'Book {self.isbn} is borrowed')
            return True
        else:
            print(f'Book {self.isbn} is not available')
            return False
