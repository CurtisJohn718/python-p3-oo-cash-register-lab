#!/usr/bin/env python3

# 1. Add items of varying quantities and prices
# 2. Calculate discounts
# 3. Keep track of what's been added to it
# 4. Void the last transaction

# Hint #1: Keep in mind that to access an attribute or call an instance method inside another instance method, 
#          we use the self keyword to refer to the instance on which we are operating.


# Hint #4: Python handles mutable default values for arguments differently than it handles immmutable default values.
#          This means that you should usually not set default values for lists, dictionaries, and instances of classes. 

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

# Hint #2: The apply_discount() method requires some knowledge about working with integers versus floats in Python. 
#          When you get to that method, take a look at what return value the test are expecting and keep in mind that Python 
#          provides methods for changing an Integer to a Float and vice versa.

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total = self.total - discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")


# Hint #3: The void_last_transaction() method will remove the last transaction from the total.
#          You'll need to make an additional attribute and keep track of the last transaction amount somehow.
#          In what method of the class are you working with an individual item?

    def void_last_transaction(self):
        self.total = self.total - self.last_transaction_amount