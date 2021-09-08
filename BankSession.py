from Bank import Bank

class BankSession:
  """ Represents the interface that one would interact with. This holds all of the
      prompts and interacts with the user and controls the flow of the bank session """
  def __init__(self, bank):
    self.bank = bank           # Needs a bank to start
    self.current_account = None # This is the account that's currently logged in

  def action(self, user_action):
    """ Contains all of the actions that a user can do """
    actions = {
        "balance": self.get_balance,
        "withdraw": self.withdraw,
        "transfer": self.transfer,
        "deposit": self.deposit,
        "history": self.get_history
    }
    return actions.get(user_action, self.wrong_input)() # use get to enable default action when mistype

  def load_user(self):
    """ Asks user if has account. If yes, asks for id and password, if not, creates on and logs in """
    result = input("Do you have an account? (yes/no) ")
    accepted_response = ["yes", "no"]
    while result not in accepted_response:
      result = input("Please enter a correct response. Do you have an account? (yes/no) ")
    if result == "yes":
      accountId = input("Enter your account id: ")
      password = input("Enter your password: ")

      found_account = self.find_account_by_id(accountId)
      if found_account and found_account.authenticate(password):
        self.current_account = found_account
        print("You are logged in")
      elif found_account and not found_account.authenticate(password):
        print("Incorrect password")
      else:
        print("Could not find an account with that id")
    else:
      first_name = input("What is your first name?: ")
      last_name = input("What is your last name?: ")
      password = input("create a password: ")
      self.current_account = self.bank.create_user_and_account(first_name, last_name, password)
    
  def display_prompts(self):
    prompt = ("\n\nWhat would you like to do next?\n"+
                "Check your balance? (balance)\n"+
                "Deposit money? (deposit)\n" +
                "Withdraw money? (withdraw)\n"+
                "Transfer funds? (transfer)\n"+
                "Get transaction history? (history)"+
                "exit (exit)")
    return input(prompt)

  def session_loop(self):
    """ This is where the user is asked the prompt. Will continuously be asked
        until the user types in exit """
    if self.current_account:
      user_response = self.display_prompts()
      while user_response != "exit":
        self.action(user_response)
        user_response = self.display_prompts()

  def get_balance(self):
    """ Get's balance of the currently logged in account """
    print(f"Your current balance is ${self.current_account.balance}")
  
  def withdraw(self):
    """ Takes an integer as an input and subtracts from balance """
    amount = int(input("How much would you like to withdraw?: "))
    response = self.current_account.withdraw(amount)
    print(response["message"])
    self.get_balance()

  def transfer(self):
    """ ---- """
    account = input("Please enter the account you would like to transfer to: ")
    amount = int(input("How much would you like to transfer?: "))

    found_account = self.bank.find_account_by_id(account)
    if found_account:
      response = self.current_account.transfer(amount, account)
      print(response["message"])
    else:
      print("Not a valid account")

  def get_history(self):
    """ Returns the transactions of the currently logged in account """
    print("This is your transaction history", *self.current_account.get_transactions())

  def deposit(self):
    """ Takes an integer as an input and adds that to balance """
    amount = int(input("How much would you like to deposit?: "))
    response = self.current_account.deposit(amount)
    print(response["message"])
    self.get_balance()
  
  def find_account_by_id(self, id):
    """ Given an id, searches for the account in the bank accounts list"""
    for account in self.bank.accounts:
      if account.account_id == id:
        return account
    return None

  def wrong_input(self):
    """ Default response when user puts a wrong input in the session loop"""
    print("You didn't enter a correct option.. Please try again")

def run():  
  # initializing bank
  bank = Bank()

  # adding users to banks records, some with balances others with no balances
  print("You can log into any of these users")
  _, account1 = bank.create_user_and_account("Isaac", "Barrezueta", "password1", 1000)
  _, account2 = bank.create_user_and_account("Dan", "C", "password2")
  _, account3 = bank.create_user_and_account("Mo", "D", "password3")

  # printing information for all accounts
  print(*bank.get_all_account_info())

  # initializing a bank session with the bank we made
  bankSession = BankSession(bank)

  # loading user and starting prompt
  bankSession.load_user()
  bankSession.session_loop()

  # Bank session closed and showing all accounts' info again
  print(*bank.get_all_account_info())


if __name__ == '__main__':
  run()