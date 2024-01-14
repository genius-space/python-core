num_1 = 100
num_2 = 10

num_3 = num_1 + num_2
print(num_3)

num_3 = num_1 - num_2
print(num_3)

num_3 = num_1 * num_2
print(num_3)

num_3 = num_1 / num_2
print(num_3)

num_1 = 7
num_2 = 2

num_3 = num_1 / num_2
num_4 = num_1 // num_2
print(num_3, num_4)

num_1 = 5
num_2 = 2

num_3 = num_1 ** num_2
print(num_3)

num_1 = 7
num_2 = 2

num_3 = num_1 % num_2
print(num_3)

num_1 = 10
num_2 = 3

num_3 = num_1 % num_2
print(num_3)

num_1 = 10
num_2 = 5

num_3 = num_1 == num_2
print(num_3)

num_3 = num_1 != num_2
print(num_3)

num_3 = num_1 < num_2
print(num_3)

num_3 = num_1 > num_2
print(num_3)

num = 10
name = "Tom"

result = num > 5 and name == "Tom"
print(result)

result = num < 5 or name == "Tom"
print(result)

result = num < 5 and name == "Tom"
print(result)

message = "Tom get some money"
print(name in message)
print(name not in message)

name = "John"
message = "You won!"
print(name in message)
print(name not in message)

age = 50
name = "Ira"
animal = "Cat"

print(age == 50 and "Ira" in name and animal != "dog")
print(age == 50 and "I" in name or animal == "dog")
print(age == 50 and "F" in name and animal != "dog")
