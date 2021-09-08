import random


class BankAccount:
  def __init__(self, BankName):
    self.BankName = "Jep's Bank"
  
  def deposit(self, num):
    self.SavingBalance = self.SavingBalance + num
    return self.SavingBalance

  def withdraw(self, num):
    self.SavingBalance = self.SavingBalance - num
    return self.SavingBalance

class SavingsAccount(BankAccount):
  def __init__(self, UserFullName, age):
    self.BankName = "Jep's Bank"
    self.UserFullName = UserFullName
    self.age = age
    self.bankAccountNumber_func()
    self.accountype(age)

  def bankAccountNumber_func(self):
    self.bankAccountNumber = random.randrange(124324, 3421454)
    return self.bankAccountNumber

  def accountype(self, age):
    if(age < 18):
      self.userAccountype = "minor account"
      return self.userAccountype
    else:
      self.userAccountype = "Adult account"
      return self.userAccountype


class CheckingAccount(BankAccount):
  def __init__(self, CheckingBalance):
    self.CheckingBalance = 0
  
  def schedulePayment(self, paymentAmount):
    pass

mychecking = SavingsAccount("jespson saint-Pierre", 24)

print(mychecking.userAccountype)