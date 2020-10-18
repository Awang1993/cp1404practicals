"""
CP1404 - Practicals
Silver Service Taxi Class
"""

from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Car that has fanciness"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi instance"""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * super().price_per_km

    def __str__(self):
        """Return a string like a Car but with flagfall added"""
        return "{}, plus flagfall of ${:.2f}"\
            .format(super().__str__(),
                    self.flagfall)

    def get_fare(self):
        """Return price for taxi trip with flagfall included"""
        current_fare = self.price_per_km * self.current_fare_distance + self.flagfall
        return round(current_fare, 1)

    def start_fare(self):
        """Begin new fare"""
        super().start_fare()

    def drive(self, distance):
        distance_driven = super().drive(distance)
        return distance_driven


