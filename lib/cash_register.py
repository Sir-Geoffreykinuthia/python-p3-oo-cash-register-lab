#!/usr/bin/env python3

 # we initialize the class with the given discount and total
class CashRegister:
    
    def __init__(self, discount=0, total=0.0):
        self.discount = discount
        self.total = total
        self.items = []
        self.item_details = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.item_details.append({'title': title, 'price': price, 'quantity': quantity})

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            discounted_total = self.total - discount_amount
            self.total = discounted_total
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if self.item_details:
            last_item = self.item_details.pop()
            last_price = last_item['price'] * last_item['quantity']
            self.total -= last_price
            last_title = last_item['title']
            self.items = self.items[:-last_item['quantity']]
        else:
            print("No items to void.")