class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

    def deposit(self, amount):
      if amount > 0:
        self.__account_balance += amount
        print("\n Deposited Rs.{}. New balance: Rs.{}".format(
            amount, self.__account_balance))
      else:
        print("\nInvalid deposit amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("\n Withdrew Rs.{}. New balance: Rs.{}".format(
          amount, self.__account_balance))
    else:
      print("\nInvalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("\nAccount balance for {}(Account #{}): Rs.{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


account = BankAccount(account_number="1236700074963",
                      account_holder_name="jeya",
                      initial_balance=6000.0)
#Test deposit and withdrawal functionality
account.display_balance()
account.withdraw(300.0)
account.withdraw(20000.0)
account.display_balance()
