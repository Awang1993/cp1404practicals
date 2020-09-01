"""
CP1404 - Basic List Operations
"""

numbers = []

print("Please enter 5 numbers")
for i in range(5):
    user_number = int(input("Number:"))
    number = numbers.append(user_number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format((sum(numbers)/len(numbers))))
