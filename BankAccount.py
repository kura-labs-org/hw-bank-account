class BankAccount:


  def __init__(self, accountNumber, name, balance):
    self.accountNumber = accountNumber
    self.name = name
    self.balance = balance
    self.transactions = []
    

  def getBalance(self): 
    print(f"Your current account balance is: ${self.balance:.2f}")

  def deposit(self, deposit):
    self.deposit = deposit
    self.balance += deposit
    print(f"You are depositing: ${deposit:.2f} ")
    self.transactions.append(f"Deposit of, amount: {deposit}")

  def withdraw(self, withdraw):
    if withdraw > 0 and self.balance > withdraw:
      self.balance -= withdraw
      print(f"You are widthdrawing: ${withdraw:.2f} ")
      self.transactions.append(f"Withdraw of, amount: {withdraw}")
    else:
      print(f"The current balance in your account is not sufficent to be widthdrawn ${withdraw:.2f} ")
     

  def transfer(self, amount, BankAccountObj):
    if amount > self.balance:
        print(f"You dont have enough in account: {self.accountNumber}")
    else:
      self.amount = amount
      self.balance = self.balance - amount
      BankAccountObj.balance = BankAccountObj.balance + self.amount
      print(f"You are transferring: ${amount:.2f} from Account Number: {self.accountNumber} to Account Number: {BankAccountObj.accountNumber}")
      self.transactions.append(f"Transfer To {self.accountNumber}, amount: {amount}")


  def displayAccount(self):
    print(f"{self.name}, Your current available balance for Account Number: {self.accountNumber} is ${self.balance:.2f}")
    self.transactions.append("Account Displayed")

b1 = BankAccount(12345, "Brittney(Checking Account)", 10.00)
b2 = BankAccount(56789, "Brittney(Savings Account)", 20.00)
b1.getBalance()
b1.deposit(13.00)
b1.displayAccount()
b1.withdraw(5.00)
b1.displayAccount()
b1.transfer(5.00,b2)
b2.displayAccount()
b1.displayAccount()