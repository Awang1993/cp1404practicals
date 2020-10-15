"""
CP1404 - Practical
Unreliable Car
"""

from Prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that is unreliable"""

    def __init__(self, name, fuel, reliability):
        """"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        distance_driven = super().drive(distance)
        if random.randint(0, 100) < self.reliability:
            return distance_driven
        else:
            return "Car is too unreliable to drive"
