# There is NO block scope in python

if 3>2:
    a_variable=10
print(a_variable)

#example
game_level=3
enemies=["Skeleton","Zombie","Alien"]
def create_enemy():
    if game_level<5:
        new_enemy=enemies[0]
    print(new_enemy)
create_enemy()

