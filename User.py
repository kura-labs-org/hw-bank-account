from random import randint

class User:
  """ Represents the a user
      currently only has first and last name. Can add methods to update other info"""
  def __init__(self, first_name, last_name):
    self.user_id = self.accountId = randint(10000,100000)
    self.first_name = first_name
    self.last_name = last_name
    self.salary = None
    self.address = None
    self.dob = None