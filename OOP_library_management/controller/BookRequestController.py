class BookRequestController:
    @classmethod
    def get_book_requests_by_string_attribute(cls, book_request_repo, message, attribute):
        content = input(message)
        return book_request_repo.get_book_requests_by_string_attribute(content, attribute)

    @classmethod
    def add_request(cls, book_request_repo, book_request):
        book_request_repo.add_request(book_request)
        print(f'{book_request} is created')

