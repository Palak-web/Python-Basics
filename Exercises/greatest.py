user1 = int(input("Enter your first num: "))
user2 = int(input("Enter your second num: "))

if user1 > user2:
    print(f"{user1} number is greater then {user2}")
elif user1 == user2:
    print(f"{user1} is equal to{user2}")
else:
    print(f"{user1} number is less then {user2}")


def input(user1, user2):

    if user1 > user2:
        print(f"{user1} number is greater then {user2}")
    elif user1 == user2:
        print(f"{user1} is equal to{user2}")
    else:
        print(f"{user1} number is less then {user2}")

input(99,10)