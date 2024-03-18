class AccountRepo:
    def __init__(self):
        self._accounts = []

    def get_accounts(self):
        return self._accounts

    def add_account(self, account):
        self.get_accounts().append(account)

    def get_member_accounts_by_string_attribute(self, value, atr):
        return [account for account in self._accounts
                if value.lower() in getattr(account, atr).lower() and account.account_type == 'member']
