"""
CP1404 Practical
Guitar Class
"""

class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, name of guitar
        year: integer, year guitar was made
        cost: float, cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def guitar_str(self):
        return "{:<20} ({}), worth $ {:10,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2020 - self.year
        return age

    def is_vintage(self, age):
        if age >= 50:
            return True
        else:
            return False
