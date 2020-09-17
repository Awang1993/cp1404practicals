"""
CP1404 - Practical 02
"""

# What did you see on line 1?
# 11, 9, 20, 13, 10, 20, 11, 7, 8, 13, 5
# What was the smallest number you could have seen, what was the largest?
# Smallest number = 5
# Largest number = 20

# What did you see on line 2?
# 9, 5, 9, 3, 9, 7, 7, 7, 3, 9
# What was the smallest number you could have seen, what was the largest?
# Smallest number = 3
# Largest number = 9
# Could line 2 have produced a 4?
# No, line 2 could not have produced a 4 as the function is set to generate every second number starting from '3'.

# What did you see on line 3?
# 2.5871147322954338, 4.385509184085565, 4.924592613153184, 4.511938040560175, 2.7986542287149225, 2.7986542287149225
# What was the samllest number you could have seen, what was the largest?
# Smallest number = 2.5
# Largest number = 5.4999999999999999

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
