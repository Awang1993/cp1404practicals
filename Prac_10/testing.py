"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    string_list = []
    for i in range(n):
        string_list.append(s)
    new_string = " ".join(string_list)

    return new_string


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def sentence_format(string):
    """
    Format string as a sentence
    >>> sentence_format('hello')
    'Hello.'
    >>> sentence_format('It is an ex parrot.')
    'It is an ex parrot.'
    """
    if string[-1] != ".":
        return string[0].upper() + string[1:] + "."
    else:
        return string[0].upper() + string[1:]


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    assert repeat_string("bye", 4) == "bye bye bye bye"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"


    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Fuel not set correctly"

    test_car.fuel = 0
    assert test_car.fuel == 0, "Fuel not set correctly"

    print(sentence_format('hello'))
    print(sentence_format('It is an ex parrot.'))

run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (don't change the tests, change the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass
