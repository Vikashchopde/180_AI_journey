
from abc import ABC, abstractmethod

class Vehicals(ABC):
    @abstractmethod
    def start(self, name):
        pass 

class Car(Vehicals):
    def start(self , name):
        print(f"car: {name} is starting")

class Bike(Vehicals):
    def start(self, name):
        print(f"bike: {name} is starting")

car = Car()
bike = Bike()

car.start("Lamborghini Urus")
bike.start("kawwasaki Ninja")

