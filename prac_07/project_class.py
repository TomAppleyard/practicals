class Project:
    def __init__(self, name="", start_date="", priority=0, money_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = money_estimate
        self.completion = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate}," \
               f" completion: {self.completion}%"

    def iscomplete(self):
        return self.completion == 100

