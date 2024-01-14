test_list = [1, 2, 3, 4, 5, 6]
for num in test_list:
    print(f"You got a {num} ---<")
    print(num ** 2)

print("-------------------------")

a = 0
while a < 10:
    print(a, "-------<")
    a += 1

print("-------------------------")

test_list = [1, 2, 3, 4, 5, 6]
while len(test_list) < 10:
    test_list.append(3)
    print(test_list)

print("-------------------------")

test_list = ["test", "python", "code"]
for s in test_list:
    print(s, "-------<")
    if s == "test":
        print(s)
    elif s == "python":
        print(s)
    else:
        print(s)

print("-------------------------")

a = 0
add_list = []
while len(add_list) < 10:
    add_list.append(a)
    a += 1
    if len(add_list) == 5:
        print("Yout are at middle of list")

print("-------------------------")

a = 0
add_list = []
while len(add_list) < 100:
    print("len of list: ", len(add_list))
    add_list.append(a)
    a += 1
    if len(add_list) == 50:
        print("Yout are at middle of list")

print("-------------------------")

user_1 = {
    "user_name": "tester",
    "role": "admin",
    "account_connection": True
}

user_2 = {
    "user_name": "junior",
    "role": "user",
    "account_connection": False
}

user_3 = {
    "user_name": "middle",
    "role": "pro_user",
    "account_connection": True
}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    print(f"Work with {user['user_name']} account -----<<<<")
    if not user["account_connection"]:
        count_of_tries = 10
        while count_of_tries != 0:
            print("Try ty connect to user account")
            count_of_tries -= 1
            print("Count of tries left: ", count_of_tries)
            if count_of_tries == 5:
                print("Middle of tries")
                continue
    elif user["role"] == "admin":
        print(f"Hello in system {user['user_name']}")
    else:
        print("Welcome on the board")

print("All users were checked!!")