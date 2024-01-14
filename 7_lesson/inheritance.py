class A:
    """Class A"""
    name_a = "class A is a parent"
    is_main_class = True

    def print_hello(self):
        print("Hello from A")


class B(A):
    """Class B"""
    name_b = "class B is a child"
    is_main_class = False

    def print_hello(self):
        print("Hello from B")
    

class C(B):
    pass


test_ex = C()
print(test_ex.name_a)
print(test_ex.name_b)
print(test_ex.is_main_class)
print(test_ex.print_hello())


class Vehicle:
    """It's a base class for Vehicles"""

    def __init__(self, type, color, left_of_life=100) -> None:
        self.type = type
        self.color = color
        self.left_of_life = left_of_life

    def move(self):
        print("Your vehicle is moving")

    def fix(self):
        if self.left_of_life <= 50:
            print(f"{self.type} need to fix")
        else:
            print(f"Your {self.type} is good")

class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, left_of_life, cost=0) -> None:
        super().__init__(type, color, left_of_life)
        self.cost = cost
    
    def move(self):
        print(f"{self.type} {self.color} is driving")
        print(f"Cost of this car: {self.cost}")


class Bicycle(Vehicle):
    """Class Bicycle"""

    def __init__(self, type, color, left_of_life, count_of_wheels) -> None:
        super().__init__(type, color, left_of_life)
        self.count_of_wheels = count_of_wheels

    def move(self):
        print("You are so fast")


car_1 = Car("car", "black", 70, 10000)
car_1.move()
car_1.fix()
bicycle_1 = Bicycle("road_bicycle", "blue", 30, 2000)
bicycle_1.move()
bicycle_1.fix()
