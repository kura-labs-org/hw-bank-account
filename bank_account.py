class BankAccount:
  def __init__(self):
    self.balance = 0
    print ("New Bank Account")

  def deposit(self):
    amount = double(input("Enter your deposit: "))
    self.balance = self.balance + amount
    print ("Your deposit has been successful %f" % self.balance)

    def withdraw(self):
      amount = float(input("Enter the amount to withdraw: "))
      if (self.balance >= amount):
          self.balance = self.balance - amount
          self.balance - self.balance - amount
          print( "Your withdrawl was successful, current balance is %f" % self.balance)
      else:
        print ('Error: Insufficient Funds!')

      Bank = BankAccount()
      Bank.deposit()

  ''' 

  Attributes:
    int account_number
    double balance
    string name
    transactions[]
  Functions:
    deposit(string this_name) -> 
    withdraw() 
    get_balance()
    transfer()

  '''