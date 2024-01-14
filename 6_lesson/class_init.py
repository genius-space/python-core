class Person:
    """Class for creation person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attrs(self):
        print(f">>>> {str(self)} <<<<")
        print(self.name, self.age)


person_1 = Person("Tom", 18)
print(person_1)
person_1.print_attrs()

person_2 = Person("Oleg", 50)
print(person_2)
person_2.print_attrs()


class Point:
    """Class for create and set coords"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.get_attrs()
        self.check_coords()

    def check_coords(self):
        for attr in self.__dict__:
            if getattr(self, attr, False) < 0 and not isinstance(self.__dict__[attr], str):
                print("Coord can't be less than 0")
                setattr(self, attr, 0)
            elif getattr(self, attr, False) > 100 and not isinstance(self.__dict__[attr], str):
                print("Coord can't be great than 100")
                setattr(self, attr, 100)
        print(self.__dict__)

    def get_attrs(self):
        print(self.__dict__)

    def set_attrs(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.check_coords()

coord_1 = Point(-1, 101, 50)

print("-----------------")
coord_1.set_attrs(1000, 1000, -5)