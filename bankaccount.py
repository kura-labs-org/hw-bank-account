import time


class BankAccount:

    numberOfAccounts = 0

    def __init__(self):
        pass
    def makeAccount(self, fullName):
        self.fullName = fullName
        self.balance = 0
        self.setAccountNumber()

    def setAccountNumber(self):
        self.accountNumber = BankAccount.numberOfAccounts + 1
        BankAccount.numberOfAccounts += 1
    
    def widthdraw(self):
        try:
            widthdrawAmount = float(input(f'''
            Balance: {self.balance}
            How much money would you like to widthdraw?
            '''))
            if(self.balance-widthdrawAmount<=0):
                print("You don't have to enough funds to complete this transaction.")
            else:
                print("Transaction complete, Thank you for choosing us.")
                self.balance -= widthdrawAmount
        except ValueError:
            print("Please a valid amount. Thanks")
        return
    def deposit(self):
        try:
            depositAmount = float(input(f'''
            Balance: {self.balance}
        How much money would you like to deposit?
        '''))
            self.balance += depositAmount
        except ValueError:
            print("Please a valid amount. Thanks")
        return
    def sendMoney(self):
        pass

    def displayName(self):
        return self.fullName
    def displayAccountNumber(self):
        return self.accountNumber
    def displayBalance(self):
        return self.balance



customer1 = BankAccount()
customer2 = BankAccount()

customer1.makeAccount("Hector")
customer2.makeAccount("Daniel")

currentCustomer = customer2

choice = "0"
while(choice!=4):
    print(''' 
    Enter (1) to Withdraw
    Enter (2) to Deposit
    Enter (3) to Send Money
    Enter (4) to Exit
''')
    choice = int(input("What would you like to do:\n"))
    if(choice==4):
        break
    else:

        choiceList = [currentCustomer.widthdraw(),currentCustomer.deposit(),currentCustomer.sendMoney()]
        choiceList[choice-1]



        print(
    f'''
    {'#'*80}
    {'*'*80}
    {time.asctime(time.localtime(time.time()))}

    Hello {currentCustomer.displayName()},    Account Number:{currentCustomer.displayAccountNumber()}

    {'*'*80}
    Balance: {currentCustomer.displayBalance()}
    {'*'*80}
    '''
    )


