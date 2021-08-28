class Bank:
    def __init__(self,accountType,accountBalance,accountName):
        self.accountType = accountType
        self.accountBalance = accountBalance
        self.accountName = accountName
        self.transactions = []
    def getTransactions(self):
        return self.transactions
    def getAccountName(self):
        return self.accountName
    def getAccountBalance(self):
        return self.accountBalance
    def getAccountType(self):
        return self.accountType
    def setTransactions(self,accountName,action):
        self.transactions.append(f"AccountID: {self.accountID}, AccountName: {self.accountName}, {action}")
        return(self.transactions)
class BankAccount(Bank):
    accountID = 0
    def __init__(self, accountType, accountBalance, accountName):
        super().__init__(accountType, accountBalance, accountName)
        BankAccount.accountID += 1
    def deposit(self,deposit):
        if deposit >= 0:
            self.accountBalance += deposit
            self.setTransactions(self.accountName,f"Added ${deposit}")
            return(*self.getTransactions(),self.getAccountBalance())
        else:
            return("Unavailable")
    def withdrawal(self,amount):
        if self.accountType is "Credit":
            self.accountBalance -= amount
            self.setTransactions(self.accountName,f"Removed ${amount}")
            return(*self.getTransactions(),self.getAccountBalance())
        else:
            if self.accountBalance >= amount:
                self.accountBalance -= amount
                self.setTransactions(self.accountName,f"Removed {amount}")
                return(*self.getTransactions(),self.getAccountBalance())
            else:
                return("Sorry Unavailable")
    def Transfer(self,BankAccountObject,cash):
        if self.accountBalance >= cash:
            self.withdrawal(cash)
            BankAccountObject.deposit(cash)
            return(self.accountBalance,BankAccountObject.accountBalance)
        else:
            return("Sorry Unavailable")
a = BankAccount("Credit",100,"Nabeel")
b = BankAccount("Debit",1000,"Test")
print(a.Transfer(b,20))
