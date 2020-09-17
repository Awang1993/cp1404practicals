"""
CP1404 Practicals
Programming Language Class
"""

class ProgrammingLanguage:
    """Represent a Programming Language object"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance.

        name: string, name of programming language
        typing: boolean, is it dynamic?
        reflection: boolean
        year, integer, year made"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def language_str(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}"\
            .format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
