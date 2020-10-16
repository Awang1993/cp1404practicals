"""
CP1404 - Practicals
Silver Service Taxi Test
"""

from Prac_08.taxi import SilverServiceTaxi


def main():
    my_silverservice = SilverServiceTaxi('Hummer', 200, 4)
    print(my_silverservice)
    my_silverservice.start_fare()
    my_silverservice.drive(100)
    print(my_silverservice.get_fare())
    print(my_silverservice)

    test_silverservice = SilverServiceTaxi('Lotus', 100, 2)
    print(test_silverservice)
    test_silverservice.start_fare()
    test_silverservice.drive(18)
    print(test_silverservice.get_fare())
    print(test_silverservice)

main()
