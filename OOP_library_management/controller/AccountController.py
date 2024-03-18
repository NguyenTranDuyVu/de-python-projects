class AccountController:
    @classmethod
    def get_member_accounts_by_string_attribute(cls, account_repo, message, attribute):
        content = input(message)
        return account_repo.get_member_accounts_by_string_attribute(content, attribute)

    @classmethod
    def check_login(cls, account_repo,username,password):
        for account in account_repo.get_accounts():
            if account.username == username and account.password == password:
                session = (account.account_type, account.account_id)
                return True, session
        return False, (None, None)
