import random
import sys


class BankAccount:
    def __init__( self ):
        self.balance = random.randint(0, 99999)
        self.history = []

    def deposit( self ):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print(" ")
        print(f"Amount Deposited: ${amount}")
        print(f"Your New Balance: ${self.balance}")
        print(" ")
        self.history.append(f"Amount Deposited: ${amount}")

    def withdraw( self ):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print(" ")
            print(f"Amount Withdrawn: ${amount}")
            print(f"Your New Balance: ${self.balance}")
            print(" ")
            self.history.append(f"Amount Withdrawn: ${amount}")
        else:
            print(" ")
            print("Insufficient Balance")
            print(f"Your Current Balance: ${self.balance}")
            print(" ")
            self.history.append(f"Withdraw Attempt Failed: Insufficient Balance")

    def transfer( self ):
        t_acc = int(input("Enter Recipient Account Number: "))
        amount = float(input("Enter amount to be be Transferred: "))
        if self.balance >= amount:
            self.balance -= amount
            print(" ")
            print(f"You have transferred: ${amount} to Account: {t_acc}")
            print(f"Your New Balance: ${self.balance}")
            print(" ")
            self.history.append(f"Transferred: ${amount} to Account: {t_acc}")
        else:
            print(" ")
            print("Insufficient Balance")
            print(f"Your Current Balance: ${self.balance}")
            print(" ")
            self.history.append(f"Transfer Attempt Failed: Insufficient Balance")

    def transactions( self ):
        print(" ")
        print("Transaction history")
        print(self.history)
        print(" ")

    def display( self ):
        print(" ")
        print(f"Available Balance: ${self.balance}")


info = BankAccount()


class OptMenu(BankAccount):
    def __init__( self ):
        super().__init__()
        print("[1] Withdraw")
        print("[2] Deposit")
        print("[3] Current Balance")
        print("[4] Transfer Money")
        print("[5] Transaction History")
        print("[q] Quit")


print("Welcome to the Barkley's Bank ATM")
print(info.display())
OptMenu()
option = input("Select an Option: ")
while option != "q" or option != "Q":
    if option == "1":
        info.withdraw()
        print("Select an Option: ")
    elif option == "2":
        info.deposit()
        print("Select an Option: ")
    elif option == "3":
        info.display()
        print("Select an Option: ")
    elif option == "4":
        info.transfer()
        print("Select an Option: ")
    elif option == "5":
        info.transactions()
        print("Select an Option: ")
    elif option == "q" or option == "Q":
        print("Thank You, Have a Nice Day")
        break
    else:
        print("Invalid Option")

    print("")
    OptMenu()
    option = input("Select an Option: ")
