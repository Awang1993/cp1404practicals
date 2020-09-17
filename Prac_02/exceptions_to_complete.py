"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        first_number = int(input("Please enter a number: "))
        while first_number != int:
            print("Please enter a valid integer.")
            first_number = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
