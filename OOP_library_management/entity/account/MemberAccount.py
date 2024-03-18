from .Account import Account

class MemberAccount(Account):
    def __init__(self, username, password,account_type,fullname, membership_date, borrowing_books=0, status='Active'):
        super().__init__(username, password, account_type, fullname,status)
        self.membership_date = membership_date
        self.borrowing_books = borrowing_books

    def __repr__(self):
        return f'{type(self).__name__}({self.account_id}, {self.account_type}, {self.fullname}, {self.membership_date}, {self.borrowing_books}, {self.status})'