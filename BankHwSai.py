from pprint import pprint
class BankAccount:
  Withdrawn = {}
  Deposited = {}
  Transfered = {}
  container = []
  def __init__(self,account_number,balance,name):
    self.account_number = account_number
    self.balance = balance
    self.name = name
  def deposit(self):
    print(f'Your current balance {self.balance}')
    depositing = float(input('How much do you want to deposit into your account?: '))
    self.balance += depositing
    self.Deposited["Deposit"] = depositing
    self.container.append(self.Deposited.copy())
    print(f'Your new balance is: {self.balance} \n')
  def withdraw(self):
    print(f'Your current balance: {self.balance}')
    withdrawl = float(input('How much do you want to withdraw from your account?: '))
    self.balance -= withdrawl
    self.Withdrawn["Withdrawl"] = withdrawl
    self.container.append(self.Withdrawn.copy())
    print(f'Your new balance is {self.balance} \n')
  def get_balance(self):
    print(f'Your current balance is {self.balance}')
  def transaction(self):
    holder = [f for f in self.container] 
    pprint(holder, width = 1)
  def transfer(self):
    transferAmount = input('How much do you want to transfer?: ')
    self.Transfered["Transfered"] = transferAmount
    self.container.append(self.Transfered.copy())

Identity = False
AccountNames = ['Sai', 'Charles']
dictBalance = {'Sai':2000, 'Charles': 1000}
while (Identity == False):
  UserInputName = input('What is your name? (enter q to quit): ')
  UserAccount = int(input('What is your account number?: '))
  if UserInputName in AccountNames and UserAccount == 1:
    Action = True
    BankObj = BankAccount(1,dictBalance[UserInputName],UserInputName)
    while Action == True:
      UserInputAction = input(f'''Hello {UserInputName}, what would you like to do today?: 
      Withdraw
      Deposit
      Transfer
      History
      Balance
      Quit
      Enter Action: ''').lower()
      if UserInputAction == 'withdraw':
        BankObj.withdraw()
      elif UserInputAction == 'deposit':
        BankObj.deposit()
      elif UserInputAction == 'transfer':
        transferName = input('who do you want to transfer money too?: ')
        if transferName in dictBalance:
          BankObj.transfer()
        else: 
          print(f'Sorry, {transferName} does not exist')
      elif UserInputAction == 'balance':
        BankObj.get_balance()
      elif UserInputAction == 'history':
        BankObj.transaction()
      elif UserInputAction == 'quit':
        Action = False

      else:
        print('You did not supply a valid operation... ')
    Identity = True
    
  elif UserInputName == 'q':
    Identity = True
  else: 
    print('You did not supply the correct user name or account number please try again')