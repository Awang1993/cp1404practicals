"""
CP1404 - Practicals
Unreliable Car Test
"""

from Prac_08.unreliable_car import UnreliableCar


def main():
    bad_car = UnreliableCar('Hyundai', 100, 50.0)
    # bad_car.drive(100)
    print("Car = {}".format(bad_car))
    print("Distance = {}".format(bad_car.drive(100)))


main()

