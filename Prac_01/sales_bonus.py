"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

RATE_LOW = .10
RATE_HIGH = .15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * RATE_LOW
        print("Your bonus is ${:.2f}".format(bonus))
        sales = float(input("Enter sales: $"))
    else:
        bonus = sales * RATE_HIGH
        print("Your bonus is ${:.2f}".format(bonus))
        sales = float(input("Enter sales: $"))
