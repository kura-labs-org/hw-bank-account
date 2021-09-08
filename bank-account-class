 '''
  Attributes:
    int account_number
    int account_number 2
    current format float amount
    str name
    str name for acct 2
    float starting balance 
    currentcy format flost ending balance

  Functions:
    get_deposit() 
    get_withdrawal() 
    get_transfer()
    display_transaction()
  '''
import datetime
x = datetime.datetime.now()

import locale
locale.setlocale( locale.LC_ALL, '' )


class Account():

  def __init__(self):

    self.s_bal = 19900.64
    self.e_bal = 0

    self.name = str(input("Please enter your name "))
    self.a_num = int(input("please enter your account number "))

    print("Hi", self.name, ", your transactions will be under ", self.a_num )
  

  def get_deposit(self):
    amt = locale.currency(float(input("Please enter your deposit amount ")))
    self.e_bal = self.s_bal + amt
    print("You deposited ", locale.currency(amt))
    print("Your balance is ", locale.currency(self.e_bal, grouping=True), " as of ", x.strftime("%x"), x.strftime("%X"))
    return self.e_bal

  def get_withdrawal(self):
    amt = float(input("Please enter your withdrawal amount "))
    self.e_bal = self.s_bal - amt
    print("You deposited ", amt)
    print("Your balance is ", locale.currency(self.e_bal, grouping=True), " as of ", x.strftime("%x"), x.strftime("%X"))
    return self.e_bal

  def get_transfer(self):
    amt = float(input("Please enter the amount you want to transfer "))
    name_2 = str(input("Who would you like to send the money to ? "))
    a_num_2 = input(" what is the account number you are transfering to? ")
    self.e_bal = self.s_bal - amt
    print("You are transferred ", locale.currency(amt, grouping=True), "to account number ", a_num_2, "for ", name_2)
    print("Your balance is ", locale.currency(self.e_bal, grouping=True), " as of ", x.strftime("%x"), x.strftime("%X"))
    return self.e_bal

  def dis_transaction(self):
    trans = input("Would you like to process a withdrawal, deposit, or transfer? ").lower()
    print(trans)
    if trans == "deposit":
      self.get_deposit()
    elif trans == "withdrawal":
      self.get_withdrawal()
    elif trans == "transfer":
      self.get_transfer()
    else:
      print("No transaction selected")
      
a = Account()
a.dis_transaction()
