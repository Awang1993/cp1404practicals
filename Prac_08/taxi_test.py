"""
CP1404 - Practical
Taxi Test
"""

from Prac_08.taxi import Taxi
from Prac_08.taxi import SilverServiceTaxi


def main():
    my_taxi = Taxi('Prius 1', 100)
    my_taxi.drive(40)
    print("Taxi = {}".format(my_taxi.name))
    print("Current fare = ${:.2f}".format(my_taxi.get_fare()))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print("Taxi = {}".format(my_taxi.name))
    print("Current fare = ${:.2f}".format(my_taxi.get_fare()))
    print(Taxi.price_per_km)

    print(SilverServiceTaxi.price_per_km)
    my_silverservicetaxi = SilverServiceTaxi('YellowCab 1', )


main()

