class Bank_account:

  def __init__(self, name, balance, account_number):
      self.name = name #attribute
      self.balance = balance #attribute
      self.acount_number = account_number #attribute
      self.transactions = {"Dunkin Donut": 11, 
                           "Target" : 22,
                           "KFC": 10,
                           "7-Eleven": 15,
                           "BP":  12.50,
                          "Best Buy":4,
                           }
  
  def deposit(self):
      cash = float(input ("Enter a positive amount of cash you want deposit into the bank account: " ))
      if cash > 0:
          self.balance += cash 
          print (f'The amount deposited is: {cash} ')
          self.transactions["Deposited"] = cash
      while cash < 0:
          print("you cannot deposit negative amount of cash")
          cash = float(input ("Enter a positive amount of cash you want deposit into the bank account: " ))
    

  def withdraw(self):
      cash = float(input("Enter the amount you want to withdraw: "))
      if cash > 0 and self.balance >= cash:
          self.balance -= cash
          print (f"You withdrew this amount: {cash} ")
          self.transactions["Withdrawn"] = cash
      elif cash < 0:
          print("you cannot withdraw negative amount of cash")
          cash = float(input ("Please enter a positive amount of cash you want to withdraw: " ))
      else:
          print("Insuficient balance in your bank account so that amount wont be able to be withdrawn")

  def transfer(self):
      another_account = int(input("Enter the account you want to transfer to: "))
      cash = float(input("Enter the amount you want transfer to that account: "))
      if cash > 0 and self.balance >= cash:
          self.balance -= cash
          print(f"The amount of:{cash}  has been transfered to the account {another_account}")
          self.transactions["transfer"] = cash
      elif cash < 0:
          print("you cannot transfer negative amount of cash")
          cash = float(input ("Enter the amount you want to transfer into the other bank account: " ))
      else:
          print("Insuficient balance so you can't transfer that amount of cash")
             
  def display_all(self):
      print (f"Net avalible Balance = {self.balance} Name = {self.name} Account number = {self.acount_number} transactions = {self.transactions}")
  
B = Bank_account("Bob", 1000000, 1234234234)
B.deposit()
B.withdraw()
B.transfer()
B.display_all()