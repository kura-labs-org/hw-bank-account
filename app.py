import random
import string
import locale
locale.setlocale( locale.LC_ALL, '' )
# function to generate a random 5 digit account number 
def genAccountNumber():


  # pick a random digit and add it to string 5 times
  account_number = ''.join(random.choice(string.digits) for i in range(5) )
  return account_number

class BankAccount:

  # record of transactions will be a list of dictionaries
  # transactions = [] error

  # record of all accounts
  accounts = []

  #initializing name, transactions, and balance
  def __init__(self,name, initial_deposit):
    self.name = name
    self.balance = initial_deposit
    self.transactions = []
    self.transactions.append({
      'deposit': initial_deposit,
      'balance': self.balance
    })

    # Call genAccountNumber to generate a random account number on initialization
    new_account_number = genAccountNumber()

    if new_account_number in self.accounts:

      self.account_number = genAccountNumber()
      self.accounts.append(self.account_number)

    else:
      self.account_number = new_account_number
      self.accounts.append(self.account_number)


  def display_accounts(self):
    print(f"All account numbers at this bank \n{self.accounts}")



  # function to check balance
  def check_balance(self):
    print(f"{self.name}'s current balance is ${self.balance}'")



  # Function to withdraw money from bank account 
  def withdraw(self):
    self.check_balance()
    withdrawal_amount = float(input('Enter the total amount you would like to withdraw'))

    if withdrawal_amount > self.balance:
      print('Not enough funds to cover withdrawal')
    else:
      self.balance -= withdrawal_amount

      # Add withdrawal to transactions list
      self.transactions.append({
          'withdrawal': withdrawal_amount,
          'balance': self.balance
      })
      print(f"Successfully withdrew ${withdrawal_amount}. \nTotal balance is now ${self.balance}")

  # Function to deposit money to bank account
  def deposit(self):
    self.check_balance()

    deposit_amount = float(input('Enter the total amount you would like to deposit'))

    if deposit_amount < 0:
      print('Stop trying to steal')

    else:
      self.balance += deposit_amount


    # Add deposit to transactions list
    self.transactions.append({
        'deposit': deposit_amount,
        'balance': self.balance
    })

    print(f"Successfully deposited ${deposit_amount} \nTotal balance is now ${self.balance}")


  # Return total list of transactions
  def getTransactions(self):
    print(f"Current List of {self.name}'s Transactions: \n{self.transactions}")


  # Method to transfer money between accounts
  
  def transfer(self,other_account): #other_account is a different instance of the BankAccount class

    # Check the balance of each account

    self.check_balance()

    other_account.check_balance()

    #Find out how much money to send

    amount_to_send = float(input(f'Enter the total amount of money you would like to send to the recipient {other_account.name}: '))

    if amount_to_send > self.balance:
      print('Not enough funds to cover transfer.')

    else:

      # Remove money from account sending money
      self.balance -= amount_to_send
      self.transactions.append({
          "Money Sent": amount_to_send,
          'balance': self.balance
      })

      print(f"{self.name} sent ${amount_to_send} to {other_account.name}: ")

      # Check sender's current balance
      self.check_balance()

      # Add money to receiving account

      other_account.balance += amount_to_send

      # Add to other accounts transaction list
      other_account.transactions.append({
          'Money Received': amount_to_send,
          'balance': self.balance
      })

      # Check the recipient's balance
      other_account.check_balance()


zach_account = BankAccount('Zach', 5000)
rando_account = BankAccount('Sara', 3000)

zach_account.deposit()

zach_account.withdraw()

rando_account.deposit()

rando_account.withdraw()

zach_account.transfer(rando_account)

zach_account.getTransactions()

print(BankAccount.accounts)

zach_account.display_accounts()
