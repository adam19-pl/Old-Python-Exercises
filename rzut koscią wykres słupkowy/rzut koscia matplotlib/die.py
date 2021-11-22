from random import randint


class Die():
    """Klasa która przedstawia kość do gry """

    def __init__(self, sides_numbers=6):
        """Proste modelowanie sześciennej kostki do gry """
        self.side_numbers = sides_numbers

    def roll_die(self):
        """Symulacja rzutu kością do gry od 1 do liczby ścianek"""
        return randint(1, self.side_numbers)


