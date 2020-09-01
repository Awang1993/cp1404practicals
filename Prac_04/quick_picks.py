"""
CP1404 - Lottery Ticket Generator
"""

import random

lottery_numbers = []

lottery_lines = int(input("How many quick picks?"))
for line in range(lottery_lines):
    lottery_number = lottery_numbers.clear() # clears the list for each line of lottery numbers
    for number in range(6):
        n = random.randint(1, 45) # generates random number
        while n in lottery_numbers: # while number exists in list, do action
            n = random.randint(1, 45)
        lottery_number = lottery_numbers.append(n) # add generated number to list
    lottery_numbers.sort() # sorts list in ascending order
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(lottery_numbers[0], lottery_numbers[1], lottery_numbers[2],
                                                       lottery_numbers[3], lottery_numbers[4], lottery_numbers[5]))
