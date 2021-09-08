class Transaction:
  """ Represents a transaction. Made it like this so bank can support all types
  of transactions in the future """
  def __init__(self, trans_type, amount, recipient = None, sender = None):
    self.trans_type = trans_type
    self.amount = amount
    self.recipient = recipient
    self.sender = sender

  def __str__(self):
    """ ALL object have an __str__ method that you can overwrite
    you just have to return a string and when you print this object, this
    is the string that will return """
    return f'type: {self.trans_type}, amount: {self.amount}, recipient: {self.recipient}'