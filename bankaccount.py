
'''
Bank account: This python program is a bank account 
with the attributes and operations below

Attributes:
    account_number
    balance
    name
Operations:
    authentication
    deposit
    withdraw
    get_balance
    transfer
'''
#Create class
class Bankaccount:

  def __init__(self):
    
    # Initialize variables
    self.name = ""
    self.balance = 0
    self.passwd = 1234
    self.login = 12345
    self.islocked_out = False

  # athentication() function will validate credentials
  # if failed for a number of time, account will be locked out
  def authentication(self):
    self.name = str (input("Enter your name: "))
    self.submitted_login = int(input("Enter your account number: "))
    self.submitted_passwd = int(input("Password: "))

    counter = 1
    while ((self.login != self.submitted_login) or (self.submitted_passwd != self.passwd)) and (counter <=1):
      print ("Attempt ", counter)
      self.account_number = int(input("Login: "))
      self.submitted_passwd = int(input("Password: "))
      counter += 1

    if (self.submitted_login == self.login or self.account_number == self.login) and (self.submitted_passwd == self.passwd):
      print ("\nWelcome to your account!\n")
    else:
      print ("Incorrect login credentials.\nToo many attempts. You are locked out of this account.")
      self.islocked_out = True

  # deposit() function will allow user to make a deposit in another account
  def deposit(self):
    if not self.islocked_out:
      print("Do you want to deposit money? (yes/no)")
      answer = input()
      if answer == "yes":
        amount = float(input("\n\nEnter the amount you want to deposit: "))
        self.balance += amount
      else:
        print("Thank you for visiting us.")

  # withdraw() function will allow user to withdraw money
  def withdraw(self):
    if not self.islocked_out:
      print("\n\nDo you want to withdraw money? (yes/no)")
      answer = str (input())
      if answer == "yes":
        wthdrw = float (input("How much do you want to withdraw? "))
        if wthdrw <= self.balance:
          self.balance = self.balance - wthdrw
          print("You enough money.")
          print("Balance after withdraw = ",self.balance)
        else:
          print("Sorry, you do not have enough money.")

  # transfer() will allow user to make a deposit in another account
  def transfer(self, other_account):
     if not self.islocked_out:
       print("\n\nDo you want to transfer money? (yes/no)")
       answer = str (input())
       if answer == "yes":
         trnsfr = float (input("How much do you want to transfer? "))
         if trnsfr <= self.balance:
           other_account.balance += trnsfr
           self.balance  = self.balance - trnsfr
           print("You enough money.")
           print("\nBalance after transfer = ",self.balance )
           print("The new account has:",other_account.balance)
         else:
           print("Sorry, you do not have enough money to transfer.")
  # display() function will display different transactions operated
  def display(self):
    if not self.islocked_out:
      print(f"Account Infos| Name: {self.name}, New balance for the old account is: $ {self.balance}, Account #: {self.login}")

print("\nWe assume the currency used is in dollars!!!\n")

object_Bank = Bankaccount()
# balance 0
object_Bank2 = Bankaccount()
# balance 0

object_Bank.authentication()
object_Bank.deposit()
object_Bank.withdraw()
object_Bank.transfer(object_Bank2)
object_Bank.display()
