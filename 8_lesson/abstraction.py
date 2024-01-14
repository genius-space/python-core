from abc import ABC, abstractclassmethod


class Car(ABC):

    def __init__(self, mark, cost) -> None:
        self.mark = mark
        self.cost = cost

    @abstractclassmethod
    def car_preview(self):
        pass


class Toyota(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")


class Mersedes(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")

    
class BMW(Car):
    pass


class Animal(ABC):
    
    @abstractclassmethod
    def move(self):
        pass


    @abstractclassmethod
    def eat(self):
        pass


class Cat(Animal):

    def __init__(self, color, age) -> None:
        self.color = color
        self.age = age


    def move(self):
        print(f"Cat with {self.color} color moves to ahead")

    
    def eat(self):
        print(f"Cat ate this food {self.age} years")



class Dog(Animal):

    def __init__(self, distance, food_type) -> None:
        self.distance = distance
        self.food_type = food_type


    def move(self):
        print(f"Dog walked {self.distance} km")

    
    def eat(self):
        print(f"Dog ate this {self.food_type} today")


class AnimalType(Animal):
    pass


class Bird(AnimalType):


    def __init__(self, name) -> None:
        self.name = name

    def move(self):
        print(f"Bird {self.name} flyes")

    
    def eat(self):
        print(f"Bird {self.name} ate two days ago")



cat = Cat("red", 7)
cat.move()
cat.eat()

dog = Dog(10, "meat")
dog.move()
dog.eat()

bird = Bird("lusy")
bird.move()
bird.eat()

animal_type = AnimalType()
animal_type.move()
animal_type.eat()
