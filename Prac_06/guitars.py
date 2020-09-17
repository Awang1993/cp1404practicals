"""
CP1404 Practicals
Guitar Program
"""

from Prac_06.Guitar import Guitar


def main():
    GUITARS = []

    print("My Guitars")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))

    guitar = Guitar(name, year, cost)
    GUITARS.append(guitar)

    print("{} ({}) : ${} added.".format(name, year, cost))

    # GUITARS.append(Guitar("Fender Stratocaster", 2014, 765.4))
    # GUITARS.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # GUITARS.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    show_guitars(GUITARS)


def show_guitars(items):
    count = 0
    for item in items:
        if item.is_vintage(item.get_age()) == True:
            count += 1
            print("Guitar {}: {}".format(count, item.guitar_str()) + " (vintage)")
        else:
            count += 1
            print("Guitar {}: {}".format(count, item.guitar_str()))


main()
