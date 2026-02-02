# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.persons = []
        self.total_height = 0
    
    def add(self, person:Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        for person in self.persons:
            self.total_height += person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.total_height} cm")
        for person in self.persons: 
            print(f"{person.name} ({person.height} cm)")
            
    def shortest(self):
        if len(self.persons) == 0:
            return None
        shortest_height = self.persons[0].height
        shortest_person = self.persons[0]
        for idx in range(1, len(self.persons)):
            if self.persons[idx].height < shortest_height:
                shortest_height = self.persons[idx].height
                shortest_person = self.persons[idx]
        return shortest_person
        
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)
        return shortest_person
        
