class BookRequest:
    id = 0

    def __init__(self, member_id, isbn, due_date,return_date=None):
        self.return_date = return_date
        self.due_date = due_date
        self.isbn = isbn
        self.id += 1
        self.borrow_code = 'BLCode-' + str(self.id)
        self.member_id = member_id

    def __repr__(self):
        return f'{type(self).__name__}({self.borrow_code}, {self.member_id}, {self.isbn}, {self.due_date}, {self.return_date})'
