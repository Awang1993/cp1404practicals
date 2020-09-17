"""
CP1404 Practical
Guitar Test Program
"""

from Prac_06.Guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    adrian = Guitar("Another Guitar", 2013, 2000)

    print(gibson.guitar_str())
    print(adrian.guitar_str())

    print(gibson.get_age())
    print(adrian.get_age())

    print(gibson.is_vintage(gibson.get_age()))
    print(adrian.is_vintage(adrian.get_age()))

    print("{} get_age() - Expected 98. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(adrian.name, adrian.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage(gibson.get_age())))
    print("{} is_vintage() - Expected False. Got {}".format(adrian.name, adrian.is_vintage(adrian.get_age())))



main()