import sys

from entity import Book, LibrarianAccount, MemberAccount, BookRequest
from repository import BookRepo, AccountRepo, BookRequestRepo
from controller import AdvertisementController, BookController, AccountController, BookRequestController
from util import Validator, Constant



def initial_data():
    member_1 = MemberAccount('m1','1','member','ng tran duy vu','01-01-2024')
    member_2 = MemberAccount('m2', '1', 'member', 'tran quang huy', '01-01-2024')
    librarian_1 = LibrarianAccount('l1','1','librarian','tran ngoc quy','01-12-2023')

    account_repo = AccountRepo()
    account_repo.add_account(member_1)
    account_repo.add_account(member_2)
    account_repo.add_account(librarian_1)

    book_1 = Book('BOOK-01', 'Lord of the Rings', 'Tolkien', '01-01-1990', 'Pearson')
    magazine_1 = Book('MAGAZINE-01', 'Car Weekly 01', 'Tien Phong authors', '01-01-2024', 'Tien Phong')

    book_repo = BookRepo()
    book_repo.add_book(book_1)
    book_repo.add_book(magazine_1)

    book_request_1 = BookRequest('ACC-1','MAGAZINE-01','01-02-2024','29-01-2024')

    book_requests_repo = BookRequestRepo()
    book_requests_repo.add_request(book_request_1)

    return account_repo, book_repo, book_requests_repo


while 1:

    # prepare initial data
    account_repo, book_repo, book_requests_repo = initial_data()

    # process login
    username_input = input('Enter username: ')
    password_input = input('Enter password: ')

    login, session = AccountController.check_login(account_repo, username_input, password_input)
    account_type, account_id = session
    # use case for member account
    if login and account_type == 'member':
        print('Login successfully')
        while 1:
            AdvertisementController.print_main_panel_member()
            match input('Enter option:'):
                # find books
                case '1':
                    AdvertisementController.print_find_books_panel_member()
                    attribute = ''
                    match input('Enter options: '):
                        case '1':
                            attribute = 'title'
                        case '2':
                            attribute = 'isbn'

                        case '3':
                            attribute = 'authors'
                        case '4':
                            attribute = 'publisher'
                        case '5':
                            continue
                        case _:
                            print('Wrong option')
                            continue
                    books = BookController.get_books_by_string_attribute(book_repo, f"Enter {attribute}: ",
                                                                         attribute)
                    print(f'There is {len(books)} suitable books')
                    for book in books:
                        print(book)
                # borrow books
                case '2':
                    AdvertisementController.print_borrow_book_panel()

                    borrowing_book_isbn = input('Enter borrowing book isbn: ')
                    borrowing_book = BookController.get_book_by_isbn(book_repo, borrowing_book_isbn)

                    if borrowing_book is None:
                        print(f'Book with isbn of {borrowing_book_isbn} is not existed')
                    else:
                        is_available = BookController.borrow_book(book_repo, borrowing_book_isbn)
                        if is_available:
                            new_book_request = BookRequest(account_id, borrowing_book_isbn, '01-12-2024', None)
                            BookRequestController.add_request(book_requests_repo, new_book_request)
                case '3':
                    continue
                case '4':
                    sys.exit()


    # use case for librarian
    if login and account_type == 'librarian':
        print('Login successfully')
        while 1:
            AdvertisementController.print_main_panel_librarian()
            match input('Enter option: '):
                # find books
                case '1':
                    AdvertisementController.print_find_books_panel_librarian()
                    attribute = ''
                    match input('Enter options: '):
                        case '1':
                            attribute = 'title'
                        case '2':
                            attribute = 'isbn'
                        case '3':
                            continue
                        case _:
                            print('Wrong option')
                            continue
                    books = BookController.get_books_by_string_attribute(book_repo, "Enter content: ",
                                                                         attribute)
                    print(f'There is {len(books)} suitable books')
                    for book in books:
                        print(book)
                # find member accounts
                case '2':
                    AdvertisementController.print_find_member_accounts_panel()
                    attribute = ''
                    match input('Enter options: '):
                        case '1':
                            attribute = 'fullname'
                        case '2':
                            attribute = 'id'
                        case '3':
                            continue
                        case _:
                            print('Wrong option')
                            continue
                    member_accounts = AccountController.get_member_accounts_by_string_attribute(
                        account_repo,f'Enter {attribute}: ', attribute)
                    print(f'There is {len(member_accounts)} suitable member accounts')
                    for acc in member_accounts:
                        print(acc)
                # find book request
                case '3':
                    AdvertisementController.print_find_book_requests_panel()
                    attribute = ''
                    match input('Enter options: '):
                        case '1':
                            attribute = 'isbn'
                        case '2':
                            attribute = 'member_id'
                        case '3':
                            continue
                        case _:
                            print('Wrong option')
                            continue
                    book_requests = BookRequestController.get_book_requests_by_string_attribute(
                        book_requests_repo, f'Enter {attribute}: ', attribute)
                    for book_request in book_requests:
                        print(book_request)
    if not login:
        print('Wrong username or password. Please reenter!')
        continue

