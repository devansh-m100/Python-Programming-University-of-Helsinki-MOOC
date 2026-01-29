# WRITE YOUR SOLUTION HERE:

class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.sum_of_weights = 0

    def add_present(self, present: Present):
        self.sum_of_weights += present.weight

    def total_weight(self):
        return self.sum_of_weights
