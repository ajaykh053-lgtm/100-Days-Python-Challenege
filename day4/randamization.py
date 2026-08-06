# Randamization and Python lists
import random

# random integer generator
random_integer = random.randint(1, 5)
print(random_integer)

# random float generator
random_float = random.random()
print(random_float)

# if we want greater than 1 in float generator sipl multiply by 10 or 100 like it
random_float = random.random() * 100
print(random_float)
ran_float = random.uniform(0, 10)
print(ran_float)

# heads or tails program using randamation
head_or_tails = random.randint(0, 1)
if head_or_tails == 1:
    print("Heads")
else:
    print("Tails")
