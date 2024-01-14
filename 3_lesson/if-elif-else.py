string = "Hello world!"
if "Hello" not in string:
    print("Hello in string")
elif "world" in string:
    print("World in string")
else:
    print("Word not in string")


a = 10
b = 20

if a == 11 and b == 20 or b <30:
    print(a + b)
else:
    print("Wrong condition")

test_list = ["hello", "test", 1, 2, 3]

if "hello" in test_list and 1 in test_list:
    print("Hello 1")
elif "test" in test_list and 4 not in test_list:
    print("Test not 4")
else:
    print("Your conditions were wrong")


a = 10
b = 20
c = "chat is active"
d = "count of users"
print(len(c), len(d), "--------<")

if len(c) >= b:
    print(c)
elif len(d) <= a:
    print(d)
else:
    print("Wrong conditions")


user_1 = {
    "name": "Tom",
    "age": 21,
    "balance": 20000,
    "currency": "USD",
    "status": True
}

user_2 = {
    "name": "John",
    "age": 17,
    "balance": 5000,
    "currency": "EUR",
    "status": False
}

user_3 = {
    "name": "Karine",
    "age": 30,
    "balance": 100000,
    "currency": "UAH",
    "status": True
}

list_of_currency = ["USD", "GBR", "UAH", "EUR"]

if user_1.get("name", None) and user_1["age"] >= 18 and user_1["status"]:
    if user_1["balance"] >= 10000 and user_1["currency"] in list_of_currency:
        print(f"Hello! You can create your binance account, welcome {user_1['name']}")
    elif user_1["balance"] >= 1000 and user_1["currency"] in list_of_currency:
        print("You need more money!")
    else:
        print ("Money critical not enough")
elif not user_1.get("name", None):
    print("Please. unite voun name in voun account desenintion")
elif user_1["age"] < 18:
    print("For registry binance account you have to be 18 year old")
else:
    print("Something went wrong")