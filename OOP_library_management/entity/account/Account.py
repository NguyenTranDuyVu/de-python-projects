from abc import ABC, abstractmethod


class Account(ABC):
    id = 0

    def __init__(self, username, password, account_type, fullname, status='Active'):
        self.username = username
        self.password = password
        self.id += 1
        self.account_id = 'ACC-' + str(self.id)
        self.account_type = account_type
        self.fullname = fullname
        self.status = status
