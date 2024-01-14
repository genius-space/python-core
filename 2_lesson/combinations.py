lst = [1, 2, 3, 4, 5]
dct = {"name": "Tom", "age": 5}
name = "Tom"
tpl = ("n", "a", "g")

result = dct["age"] in lst
print(result)

result = dct["age"] in lst and dct["name"] in tpl
print(result)

check = None

print(dct["name"] == name and dct["age"] in lst)