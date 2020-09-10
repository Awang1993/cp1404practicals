"""
CP1404 Practical
Word Occurrences
"""

WORD_COUNT = {}

input_str = input("Please enter a string: ")
for word in input_str.split():
    if word in WORD_COUNT:  # If word is in word count, word count + 1
        WORD_COUNT[word] += 1
    else:  # If word NOT in word count, word count = 1
        WORD_COUNT[word] = 1
for key, value in sorted(WORD_COUNT.items()):  # Sort dictionary and print each key and value
    # print('{{}:{}{width}}'.format(key, value, width='10'))
    # print("{:{}} = {:10}".format(key, value)