class Bank_account:
  def __init__(self, account_number,account_balance, name ):
    self.account_number = account_number
    self.account_balance = account_balance
    self.name = name 
  def deposit(self):
    deposit = int(input(f"Hey {self.name} How much did you want to deposit today?  "))
    self.account_balance += deposit 
    print(f' Your current balance is {self.account_balance }')
    return deposit
  def withdrawal(self):
    withdrawal =  int(input(f"How much did you want to withdraw today?  "))
    self.account_balance -= withdrawal
    print(f'Your current balance is {self.account_balance}')
    return withdrawal 
  def transfer(self)
    pass
bank_account1 = Bank_account (346318,37000, 'Steve')
bank_account1.deposit()
bank_account1.withdrawal()
