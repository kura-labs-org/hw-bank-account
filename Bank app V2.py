class ATM():
    Id_num = 23091

    def __init__(self,name,balance):
      self.account_N = ATM.Id_num
      self.name= name
      self.balance = balance
      ATM.Id_num += 1

    def getname_id(self):
      return print(f"Welcome {self.name} Account# {self.account_N}\nYour balance is {self.balance} ")
    
    def Withdraw(self):
      amount= float(input("Enter the amount to be withdraw: "))
      if amount > self.balance:
          print(f"{self.name},try again you don't have sufficiency money to compelete this transaction")
      else:
           self.balance -= amount
           print(f"{self.name}, you have {self.balance} in your account")
    
    def Deposit(self):
      amount=float(input("Enter the amount to be deposited: "))
      self.balance += amount
      return  print(f"{self.name}, you have {self.balance} in your account")

      
    def transferto(self,internalObject):
      print(f"You are sending funds from  {self.account_N}  to -->  {internalObject.account_N}")
      amount = int(input("How much would you like to transfer? "))
      if amount > self.balance:
        print(f"{self.name}  you don't have that much in your account.")
      else:
        self.balance -= amount
        internalObject.balance = internalObject.balance + amount
        print(f"Account: {self.account_N}  You now have  {self.balance}  remaining in your account")
        print(f"Account: {internalObject.account_N}  You now have  {internalObject.balance}  remaining in your account")
      

name1 = "leon"
balance1=5000
account1 =ATM(name1,balance1)
account1.getname_id()
# account1.Withdraw()
# account1.Deposit()

name2 = "John"
balance2=3000
account2 =ATM(name2,balance2)
# account2.getname_id()
# account2.Withdraw()
# account2.Deposit()

account1.transferto(account2)
account2.getname_id()