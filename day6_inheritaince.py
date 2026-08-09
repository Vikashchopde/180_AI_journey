class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def voice(self, breed):
         super().eat()
         print(f"{self.name} is a {breed} and say woof woof")

class Cat(Animal):
    def voice(self, breed):
         super().eat()
         print(f"{self.name} is a {breed} and say meow meow") 


class Lion(Animal):
    def voice(self, breed):
        super().eat()
        print(f" {self.name} is a {breed} and say roar roar") 


dog = Dog("frenky")   
dog.voice("german shepherd")
cat = Cat("kitty")
cat.voice("persian cat")
lion = Lion("simba")
lion.voice("african lion")



class vehicle:
    def __init__(self, name):
        self.name = name 

    def start(self):
        print(f"{self.name} is starting.")


class Car(vehicle):
    def drive(self, model):
        super().start()
        print(f"{self.name} is a {model} and is driving.")

class Bike(vehicle):
    def drive(self, model):
        super().start()
        print(f"{self.name} is a {model} and is riding.")


car = Car("Lamborghini")
car.drive("Urus")

bike = Bike("Ducati")
bike.drive("Panigale")
