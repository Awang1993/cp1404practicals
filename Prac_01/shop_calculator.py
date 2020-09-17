"""
CP1404/CP5632 - Practical
Shop Calculator
"""

total_price = 0
discount_offer = .1
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_cost = float(input("Price of item: "))
    total_price = total_price + item_cost
if total_price > 100:
    total_price = total_price - (total_price * discount_offer)
print("Total price for {} items is {:.2f}".format(number_of_items, total_price))
