class Bank_Account:
  def __init__(self, name, balance=0):
   self.name = name
   self.balance = balance
   print(f"Hello!! Welcome {self.name}")
  
  def deposit(self):
        amount = float(input("Enter the amount to be deposited: "))
        self.balance += amount
        print(f"{self.name} deposited: , {amount}")

    
  def withdraw(self):
        amount = float(input("Enter the amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print(f"{self.name} withdrew: {amount} today")
        else:
            print(f"Insufficient balance  ")
    
  def display(self):
        print(f"Your Net Available Balance=: ", self.balance)
    
    # creating an object of class
b1 = Bank_Account("Mary", 300)
   
# Calling functions with that class object
b1.deposit()
b1.withdraw()
b1.display()
