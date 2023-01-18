from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name='', fuel=0, reliability=0.0):
        """Initialise an UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car depending on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
