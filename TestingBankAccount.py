import sys

class BankAccount:
  def __init__(self, name, accountNumber):
    self.name = name
    self.accountNumber = accountNumber
    self.balance = []

  def addToBalance(self):
    if len(self.balance) == 0:
      print("you have no money")
      self.balance.append(0)
      amount_to_add = abs(float(input("How much do you want to add to the balance? ")))
      response = input(f"You're looking to deposit {amount_to_add} to the account, is that right (y/n)? ")
      if response in ["y", "yes", "YES",]:
        self.balance.append(self.balance[-1] + amount_to_add)
        print(f'Your new balance is now {self.balance[-1]} ')
      else:
        print("You didn't put a proper response. Ending session now! ")
        sys.exit(0)
    else:
      print(f"you have {self.balance[-1]}")
      amount_to_add = abs(float(input("How much do you want to add to the balance? ")))
      response = input(f"You're looking to deposit {amount_to_add} to the account, is that right (y/n)? ")
      if response in ["y", "yes", "YES",]:
        self.balance.append(self.balance[-1] + amount_to_add)
        print(f'Your new balance is now {self.balance[-1]} ')
      else:
        print("You didn't put a proper response. Ending session now! ")
        sys.exit(0)
    
  def subFromBalance(self):
    if len(self.balance) == 0:
      print("you have no money")
      self.balance.append(0)
      amount_to_sub = abs(float(input("How much do you want to witdraw from balance? You will owe the bank if you withdraw ")))
      response = input(f"You're looking to withdraw {amount_to_sub} to the account, is that right (y/n)? ")
      if response in ["y", "yes", "YES",]:
        self.balance.append(self.balance[-1] - amount_to_sub)
        print(f'Your new balance is now {self.balance[-1]} . Please pay us back!')
      else:
        print("You didn't put a proper response. Ending session now! ")
        sys.exit(0)
    else:
      print(f"you have {self.balance[-1]}")
      amount_to_sub = abs(float(input("How much do you want to withdraw from this balance? ")))
      response = input(f"You're looking to deposit {amount_to_sub} to the account, is that right (y/n)? ")
      if response in ["y", "yes", "YES",]:
        self.balance.append(self.balance[-1] + amount_to_sub)
        print(f'Your new balance is now {self.balance[-1]} ')
      else:
        print("You didn't put a proper response. Ending session now! ")
        sys.exit(0)
  def presentBalance(self):
    if self.balance:
      print("You have no money!")
    else:
      print(f"You currently have {self.balance[-1]}")

def accountmaker(x):
  try:
    x
  except NameError:
    x = BankAccount(f"{user_name}",12354)
  else:
    print("You Have an Account!")

user_input = input("Please type your name and birthday(MMDD) (Example: Kawang0123")
user_name = user_input[0:-4]
listing = []
listing.append(user_input)
print(f'Your name is {user_name}')
print(f'You typed {user_input}')

accountmaker(listing[0])
print(type(Kawang0123))
theaccount = listing[0]
theaccount.addToBalance()
# account2.presentBalance()

'''The intention in this change is to use a user input as a variable name, then utilize a function to create a bank class if no bank classes are found. Have already tried using globals()[user_input]'''
