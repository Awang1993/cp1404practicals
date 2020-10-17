"""
CP1404 - Practicals
Taxi Simulator
"""

from Prac_08.silver_service_taxi import SilverServiceTaxi
from Prac_08.taxi import Taxi


def main():

    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_bill = 0
    total_bill = 0
    current_taxi = ""

    print("Let's drive!")
    menu_option = input("q)uit, c)hoose, d)rive\n>>>").lower()
    while menu_option != 'q':
        if menu_option == 'c':
            display_taxi(taxis)
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[chosen_taxi]
            # print(current_taxi)#
            display_bill(total_bill, current_bill)
            menu_option = input("q)uit, c)hoose, d)rive\n>>>").lower()
        if menu_option == 'd':
            travel_distance = int(input("Drive how far?"))
            current_taxi.start_fare()
            current_taxi.drive(travel_distance)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            total_bill += current_taxi.get_fare()
            display_bill(total_bill, current_bill)
            menu_option = input("q)uit, c)hoose, d)rive\n>>>").lower()


def display_taxi(taxis):
    count = 0
    for taxi in taxis:
        print("{} - {}".format(count, taxi))
        count += 1


def display_bill(total_bill, current_bill):
    total_bill += current_bill
    print("Bill to date: ${:.2f}".format(total_bill))


main()
