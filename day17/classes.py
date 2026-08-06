# Creating classs
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "latha")
user_2 = User("002", "Ajay")
user_1.follow(user_2)
user_2.follow(user_1)

print(user_1.user_id)
print(user_1.username)
print(user_1.follower)
print(user_1.following)
print(user_2.user_id)
print(user_2.username)
print(user_2.follower)
print(user_2.following)


# Constractor


# syntax
def __inti__(self):
    pass


#    how to add attributes to Constarctor
class Car:
    def __init__(self, seats):
        self.seats = seats


my_car = Car("5")


# Class method
# calling methods to changes attributes inside the class
class Car:
    def enter_race_mode(self):
        self.seats = 2


my_car.enter_race_mode()
