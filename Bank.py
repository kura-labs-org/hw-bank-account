from Account import Account
from User import User

class Bank:
  """ Bank's job is to keep a record of all accounts and users
      A bank can also create a user or an account or both """
  def __init__(self):
    self.users = [] # list of Users
    self.accounts = [] # list Accounts
  
  def create_user_and_account(self, first_name, last_name, password, bal = 0):
    """ Uses firstname, lastname, and password to create user.. Can pass a balance (int)
        returns tuple of user and account that was created """
    new_user = self.create_user(first_name, last_name)
    new_account = self.create_account(new_user, password, bal)
    return (new_user, new_account)

  def create_account(self, user, password, bal):
    """ Uses user/password bal to make an account
        returns the account that was created """
    new_account = Account(user, bal)
    new_account.set_password(password)
    new_account.bank = self
    self.accounts.append(new_account)
    return new_account
  
  def create_user(self, first_name, last_name):
    """ Uses firstname, lastname to make user
        returns the user that was created """
    new_user = User(first_name, last_name)
    self.users.append(new_user)
    return new_user
  
  def find_account_by_id(self, id):
    for account in self.accounts:
      if account.account_id == id:
        return account
    return None
  
  def get_all_account_info(self):
    """ Returns a string of account info determined by Account.get_account_info() """
    return [acct.get_account_info() for acct in self.accounts]





