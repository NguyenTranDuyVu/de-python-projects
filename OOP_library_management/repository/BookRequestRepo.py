class BookRequestRepo:
    def __init__(self):
        self._book_requests = []

    def get_book_requests_by_string_attribute(self, value, atr):
        return [book_request for book_request in self._book_requests if
                value.lower() in getattr(book_request, atr).lower()]

    def add_request(self, book_request):
        self._book_requests.append(book_request)
