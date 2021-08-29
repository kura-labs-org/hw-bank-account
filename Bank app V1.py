class ATM():

    def __init__(self,name,account_N,balance):
      self.account_N = account_N
      self.name= name
      self.balance = balance

    def getname_id(self):
      return print(f"Welcome {self.name} Account# {self.account_N} ")
    
    def getbalance(self):
      return self.balance

    def Withdraw(self):
      amount= float(input("Enter the amount to be withdraw:"))
      balance1 = self.balance - amount
      return balance1
    
    def Deposit(self):
      amount=float(input("Enter the amount to be deposited:"))
      balance1 = self.balance + amount
      return balance1

name1 = "leon"
account1=1123
balance1 = 5000
l_atm =ATM(name1,account1,balance1)
l_atm.getname_id()
l_atm.Withdraw()
# l_atm.Deposit()