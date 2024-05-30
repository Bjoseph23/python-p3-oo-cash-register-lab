class CashRegister:

  def __init__(self, discount=0): 
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.items.append({"title": title, "price": price, "quantity": quantity})
    self.total += price * quantity

  def apply_discount(self):
    if self.discount > 0:  
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount
      print(f"After the discount of {self.discount}%, the total comes to ${self.total:.2f}.\n")
    else:
      print("There is no discount to apply.\n")

  def void_last_transaction(self):
    if self.items:
      last_item = self.items.pop()
      self.total -= last_item["price"] * last_item["quantity"]
      if not self.items:
        self.total = 0

  def get_total(self):
    print(f"You have a total of ${self.total}")

  def get_items(self):
    return self.items.copy()  

# Example usage
cash_register = CashRegister(discount=30)
cash_register.add_item("eggs", 2.50,2)

cash_register.apply_discount()

print(cash_register.get_total())

print(cash_register.get_items())
