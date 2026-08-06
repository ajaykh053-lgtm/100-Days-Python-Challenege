# LISTS IN PYHON
friends = ["Ajay"]  # creating the list in pyhton
# friends.append(['Adithy','chandu'])#adding item of list to the list
# adding item to list
friends.append("mohan")
friends.append("manu")
friends.append("narshima")
friends.append("vishwa")
print(friends)  # printing the items from the list all items
print(friends[2])
print(friends[1])
print(friends[3])
print(friends[4])
print("\n")

import random

# option mo 1
randomone = random.choice(friends)
print("pay the bill:", randomone)
# option no 2
randomindex = random.randint(0, 4)
print("\n", friends[randomindex])


# nested lists
fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]


print(dirty_dozen)
print("\n")
print(dirty_dozen[0])
print("\n")
print(dirty_dozen[1])
print("\n")
print(dirty_dozen[1][0])
print("\n")
print(dirty_dozen[1][1])
print("\n")
print(dirty_dozen[1][2])
print("\n")
print(dirty_dozen[1][3])
print("\n")

print(dirty_dozen[0][0])
print("\n")
print(dirty_dozen[0][1])
print("\n")
print(dirty_dozen[0][2])
print("\n")
print(dirty_dozen[0][3])
print("\n")
print(dirty_dozen[0][4])
print("\n")
print(dirty_dozen[0][5])
print("\n")
