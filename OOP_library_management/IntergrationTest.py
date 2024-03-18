from entity import Book
from repository import Catalog
from util import Validator, Constant

def test_catalog():
    b1 = Book('BOOK-01', 'Lord of the Rings', 'Tolkien', '01-01-1990', 'Pearson')
    m1 = Book('MAGAZINE-01', 'Car Weekly 01', 'Tien Phong authors', '01-01-2024', 'Tien Phong')

    catalog = Catalog()

    catalog.add_book(b1)
    catalog.add_book(m1)

    catalog.borrow_book('BOOK-01')
    catalog.borrow_book('BOOK-01')
    print(catalog.get_books_by_string_attribute('', 'title'))


def test_validator():
    print(Validator.get_from_a_list('Enter input', Constant.test))

test_catalog()