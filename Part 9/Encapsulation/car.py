# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km:int):
        if self.__petrol >= km:
            self.__petrol -= km
            self.__odometer += km
        elif self.__petrol < km and self.__petrol != 0:
            self.__odometer += self.__petrol
            self.__petrol = 0
        
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"
