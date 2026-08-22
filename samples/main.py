class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance = self.balance + amount
      print(f"Deposited {amount}")
    return self.balance

  def withdraw(self, amount):
    if 0 < amount and amount <= self.balance:
      self.balance = self.balance - amount
      print(f"Withdrew {amount}")
    else:
      print("Insufficient funds")
    return self.balance

account = BankAccount("Bob", 200)
account.deposit(100)
account.withdraw(50)
print(f"Balance: {account.balance}")