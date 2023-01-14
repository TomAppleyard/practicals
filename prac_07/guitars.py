class Guitars:

    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.year}) - {self.price}"

    def __lt__(self, other):
        return self.year < other.year


