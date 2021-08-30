class BankAccount:
        def __init__(self):
                self.balance=0
                print("Deposit/Withdrawal Machine")

        def deposit(self):
                x=float(input("Enter Deposit Amount"))
                self.balance += x
                print("\n Amount Deposited:")
                print(self.balance)

        def withdraw(self):
                x = float(input("Enter Withdrawn Amount:"))
                if self.balance >= x:
                      self.balance -= x
                      print("\n Amount Withdrew:", x)
                else:
                      print("\n Insufficient balance")

        def display(self):
                print("\n Account Balance=",self.balance)


b = BankAccount()
b.deposit()
b.withdraw()
b.display()
