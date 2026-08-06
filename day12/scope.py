enemies = 1


def increase_enemis():
    enemies = 2
    print(f"enemies inside fucntion is : {enemies}")


increase_enemis()
print(f"enemies inside fucntion is : {enemies}")

# Loacal scope"""""""""""""""""""""


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength)#error show undeffined error

# Gobal scope"""""""""""""""""""

player_life = 10


def drink_potion():
    potion_strength = 2
    print(player_life)


drink_potion()

# Modifing Gobal varable
enemies = 1


def increase_enemis():
    global enemies
    enemies = 2
    print(f"enemies inside fucntion is : {enemies}")


increase_enemis()
print(f"enemies inside fucntion is : {enemies}")

enemies = 1


def increase_enemis(enemy):
    print(f"enemies inside fucntion is : {enemies}")
    return enemy + 1


enemies = increase_enemis(enemies)
print(f"enemies outside fucntion is : {enemies}")
