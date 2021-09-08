class BankAccount: 
  def __init__(self, acct_name, acct_num, checkings_balance, savings_balance):
    self.acct_name = acct_name
    self.acct_num = acct_num
    self.checkings_balance = float(checkings_balance)
    self.savings_balance = float(savings_balance)
  
  def customer_login(self):
    cust_username = input("Enter your username: ")
    cust_passwd = input("Enter your password: ")
    print("Login successful ")

  def display_checkings_balance(self): 
    print(f"Your current checkings balance is ${self.checkings_balance}")

  def display_savings_balance(self):
    print(f"Your current savings balance is ${self.savings_balance}")  

  def make_deposit(self):
    amount = float(input("Enter your deposit: "))
    if amount > 0:
      self.checkings_balance += amount
      print(f"Your current balance is ${self.checkings_balance}")

  def make_withdrawl(self):
    amount = float(input("How much do you want to withdrawl? $"))
    if amount > 0:
      self.checkings_balance -= amount
      print(f"Your current balance is ${self.checkings_balance}")

  def transfer_from_checkings_to_savings(self):
    amount = float(input("How much would you like to transfer? $"))
    if amount > 0.00:
      self.checkings_balance -= amount
      self.savings_balance += amount
      print(f"Your current checkings balance is ${self.checkings_balance}")
      print(f"Your current savings balace is ${self.savings_balance}")

  def transfer_btn_accounts(self, acct_name):
      amount = float(input("How much would you like to transfer? $"))
      if amount > self.checkings_balance:
         print("You have insufficient funds.")
      elif amount > self.checkings_balance:
         self.checkings_balance < amount
         self.checkings_balance = self.checkings_balance - amount
         acct_name.checkings_balance = acct_name.checkings_balance + amount
         print(f"{acct_name.acct_name}'s new checkings balance is ${acct_name.checkings_balance}")
         print(f"{self.acct_name}'s new checkings balance is ${self.checkings_balance}") 
      else:
         print("You have insufficient funds.")  

b1 = BankAccount("Maisha Ahmed", 10000000, 1000.00, 1000.00)
b2 = BankAccount("Brittney Jones", 10000001, 1100.00, 1100.00)
b1.customer_login()
b1.display_checkings_balance()
b1.display_savings_balance()
b1.make_withdrawl()
b1.transfer_from_checkings_to_savings()
b1.make_deposit()
b1.display_checkings_balance()
b1.transfer_btn_accounts(b2)

b2 = BankAccount("Brittney Jones", 10000001, 1100.00, 1100.00)
b2.customer_login()
b2.display_checkings_balance()
b2.display_savings_balance()
b2.make_deposit()
b2.display_checkings_balance()