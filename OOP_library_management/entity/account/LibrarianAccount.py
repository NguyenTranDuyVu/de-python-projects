from .Account import Account

class LibrarianAccount(Account):
    def __init__(self, username, password, account_type,fullname, starting_date, status='Active'):
        super().__init__(username, password,account_type, fullname, status)
        self.starting_date = starting_date

    def __repr__(self):
        return f'{type(self).__name__}({self.account_id}, {self.account_type}, {self.fullname}, {self.starting_date}, {self.status})'



