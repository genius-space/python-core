# Funcs for int
num_1 = "1"
print(type(num_1))

num_1 = int(num_1)
print(type(num_1))

num_1 = float(num_1)
print(type(num_1))

# Funcs for string
string = "hello world!"
print(len(string))

string = string.upper()
print(string)

string = string.lower()
print(string)

string = string.capitalize()
print(string)

string = string.replace("!", ".")
print(string)

string = string.split()
print(string)

string = " ".join(string)
print(string)

string = string.count("o")
print(string)

string = 1
string = str(string)
print(type(string))

# Funcs for list
base_list = [1, 2, 3]
print(len(base_list))

base_list.append(4)
print(base_list)

base_list.extend([5, 6, 7])
print(base_list)

print(base_list.index(4))

# Funcs for dict
base_dict = {"name": "Tom", "age": 40, "high": 180}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items())

print(base_dict["name"], base_dict.get("name"), base_dict.get("is_animal", "No"))
print(base_dict["is_animal"])