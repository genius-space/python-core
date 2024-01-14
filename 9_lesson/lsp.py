class Car:
    def __init__(self, type) -> None:
        self.type = type
        self.properties = {}
    
    def set_propetries(self, color, cost, capacity):
        self.properties = {"Color": color, "Cost": cost, "Capacity": capacity}

    def get_properties(self):
        return self.properties


class PetrolCar(Car):
    def __init__(self, type) -> None:
        self.type = type
        self.properties = {}


car = Car("Toyota")
car.set_propetries("Red", 10000, 6)

petrol_car = PetrolCar("Volvo")
petrol_car.set_propetries("Blue", 5000, 4)

cars = [car, petrol_car]

def get_concret_color_car(color):
    count = 0
    car_types = []
    for car in cars:
        if car.properties["Color"] == color:
            count += 1
            car_types.append(car.type)
    
    print(f"Count of {color} cars: {count}\nCat types: {car_types}")

get_concret_color_car("Blue")