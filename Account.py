from Transaction import Transaction
class Account:
  """ Account represents an individual account. An account holds all of the
      information and behaviors needed for working with an account.
      password for Authenticating user, transaction capabilities like depositing,
      viewing balance and seeing all account info """

  subtract_types = ["Withdrawal", "Transfer"] # Used to determin how to handle transaction
  account_number_counter = 189866

  def __init__(self, user, bal = 0):
    Account.account_number_counter += 1
    self.account_id = str(Account.account_number_counter)
    self.balance = bal                    # total balance
    self.user = user                      # User object associated with this account
    self.transactions = []                # will hold all transactions
    self.password = None
    self.bank = None

  def validate_transaction(self, transaction):
    """ Given a transaction, we check it's type and check the balance supports
        the transaction.
        returns an object with transaction status and message """
    if transaction.trans_type in self.subtract_types:
      if transaction.amount > self.balance:
        return {"status": "failed", "message": "Insufficient Funds"}
    if transaction.trans_type == "Transfer":
      self.alert_bank_of_transfer(transaction)
    self.update_balance(transaction)
    self.transactions.append(transaction)
    return {"status": "passed", "message": f'Your {transaction.trans_type} was successful'}

  def set_password(self, password):
    self.password = password

  def update_balance(self, transaction):
    """ Given a transaction, adds or subtracts to balance """
    if transaction.trans_type in self.subtract_types and transaction.recipient != self.account_id:
      self.balance -= transaction.amount
    else:
      self.balance += transaction.amount

  def withdraw(self, amount):
    """ Create a transaction of withdrawal type and validates """
    withdrawal = Transaction("Withdrawal", amount)
    return self.validate_transaction(withdrawal)
  
  def deposit(self, amount):
    """ Create a transaction of deposit type and validates """
    deposit = Transaction("Deposit", amount)
    return self.validate_transaction(deposit)

  def transfer(self, amount, account):
    """ Create a transaction of transfer type and validates """
    transfer = Transaction("Transfer", amount, account, self.account_id)
    return self.validate_transaction(transfer)
  
  def recieve_transfer(self, transfer):
    self.update_balance(transfer)
  
  def authenticate(self, password):
    """ returns whether password given matches password on record """
    return password == self.password
  
  def get_transactions(self):
    """ returns transaction history """
    return self.transactions
    
  def get_account_info(self):
    """ returns string of account info """
    return f'|({self.user.first_name} {self.user.last_name}) {self.account_id} : ${self.balance} {self.password} |'

  def alert_bank_of_transfer(self, transfer):
    account = self.bank.find_account_by_id(transfer.recipient)
    if account is not None:
      account.recieve_transfer(transfer)
      return {"status": "passed", "message": f"recipient recieved transfer of {transfer.amount}"}
    else:
      return {"status": "failed", "message": f"Transfer failed"}