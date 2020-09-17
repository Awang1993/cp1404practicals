"""
CP1404 - Practical
1. Write code that asks the user for their name, then opens a file called "name.txt" and
writes that name to it.
2. Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
3. Create a text file called numbers.txt and save it in your prac_02 directory. Put the following
three numbers on seperate lines in the file and save it.
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together
then prints the result, which should be... 59.
4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file
with any number of numbers.
"""

# 1. Write code that asks the user for their name, then opens a file called "name.txt" and
# writes that name to it.
# OUTPUT_FILE = "name.txt"
#
# out_file = open(OUTPUT_FILE, 'w')
# name = input("What is your name: ")
# print(name, file=out_file)
#
# out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
# INPUT_FILE = "name.txt"
#
# in_file = open(INPUT_FILE).read()
# print("Your name is {}".format(in_file))
#
# in_file.close()

# 3. Create a text file called numbers.txt and save it in your prac_02 directory. Put the following
# three numbers on seperate lines in the file and save it.
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together
# then prints the result, which should be... 59.

# numbers = [17, 42, 400]
#
# OUTPUT_FILE = "numbers.txt"
# INPUT_FILE = "numbers.txt"
#
# out_file = open(OUTPUT_FILE, 'w')
# for number in numbers:
#     print(number, file=out_file)
#
# out_file.close()
#
# in_file = open(INPUT_FILE, 'r')
# first_number = int(in_file.readline())
# second_number = int(in_file.readline())
# print(first_number + second_number)
#
# in_file.close()

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file
# with any number of numbers.

INPUT_FILE = "numbers.txt"

total = 0

in_file = open(INPUT_FILE, 'r')

for line in in_file:
    total += int(line)
    # print(total)
print(total)
