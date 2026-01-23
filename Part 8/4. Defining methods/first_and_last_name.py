# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.name = name
    
    def return_first_name(self):
        name_split = self.name.split(" ")
        return name_split[0]

    def return_last_name(self):
        name_split = self.name.split(" ")
        return name_split[-1]












