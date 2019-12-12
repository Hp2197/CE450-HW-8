class VndMchn():
  def __init__(self, item, price):
    self.item = item
    self.price = price
    self.stock = 0
    self.cash = 0
  def vending(self):
    if self.stock > 0:
      if self.cash < self.price:
        return str("Need to deposit $" + str(self.price - self.cash) + " more.")
      elif self.cash == self.price:
        self.cash = 0
        self.stock -= 1
        return "Take your soda"
      else:
        temp = self.cash - self.price
        self.cash = 0
        self.stock -= 1
        return "Take your soda and $" + str(tmp) + " change."
    else:
      return "Out of stock currently"
  def adding(self, x):
    self.stock += x
    return "Current " + self.item + " stock: " + str(self.stock)
  def deposit(self, x):
    if self.stock > 0:
      self.cash += x
      return "Current balance : $" + str(self.cash)
    else:
      return "Out of stock. Returning to you: $" + str(x)