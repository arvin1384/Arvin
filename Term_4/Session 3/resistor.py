from colors import *


class resistor:
    def __init__(self, hundreds="Black", decimal="Black", ten_power="Black"):
        self.resistance = 0
        self.hundreds = colors[hundreds]
        self.decimal = colors[decimal]
        self.ten_power = colors[ten_power]
        self.calculate_resistance()

    def calculate_resistance(self):
        self.resistance = self.hundreds
        self.resistance *= 10
        self.resistance += self.decimal
        for i in range(self.ten_power):
            self.resistance *= 10
        return self.resistance

    def __eq__(self, other):
        return self.calculate_resistance() == other.calculate_resistance()

    def __lt__(self, other):
        return self.calculate_resistance() < other.calculate_resistance()

    def __le__(self, other):
        return self.calculate_resistance() <= other.calculate_resistance()

    def __gt__(self, other):
        return self.calculate_resistance() > other.calculate_resistance()

    def __ge__(self, other):
        return self.calculate_resistance() >= other.calculate_resistance()
