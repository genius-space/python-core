test_dict = {"user": "Oleg", "age": 21, "country": "Poland"}
print(test_dict["user"], test_dict["age"], test_dict.get("country"))
print(test_dict.get("animal", "key not found"))
test_dict["age"] = 30
print(test_dict ["age"])
test_dict[ "animal"] = "cat"
print(test_dict["animal"])
animal = test_dict.pop("animal")
print(animal)

copy_test = test_dict.copy()
test_dict.clear()
print(test_dict, "<-copied->", copy_test)

for key, value in copy_test.items():
    print(f"Key: {key}, Value: {value}")

for value in copy_test.values():
    print(value)

wrong_key = copy_test.pop("currency", "key not found")
print(wrong_key)


dict_update = {"new_role": "admin", "salary": 10000}
copy_test.update(dict_update)
print(copy_test)