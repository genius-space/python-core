class Person:
    """Class for creation person"""
    name = "Tom"
    age = 18
    high = 180

print(Person.name, Person.age)
Person.age = 50
print(Person.name, Person.age)
print(Person.__dict__)

person_1 = Person()
print(person_1)
print(person_1.name, person_1.age, person_1.high)

person_2 = Person()
print(person_2)
print(person_2.name, person_2.age, person_2.high)

person_1.is_animal = False
print(person_1.__dict__)
print(Person.__dict__)
print(person_2.__dict__)

print(getattr(person_1, "name"))
print(getattr(person_1, "where_is", False))

person_1.age = 59
person_1.color = "black"
print(person_1.__dict__)

setattr(person_1, "high", 100)
print(person_1.high)
print(person_1.__dict__)

print(hasattr(person_1, "name"))
print(hasattr(person_1, "where_is"))

del Person.high
print(Person.__dict__)
print(hasattr(Person, "high"))

delattr(Person, "age")
print(Person.__dict__)
print(hasattr(Person, "age"))
