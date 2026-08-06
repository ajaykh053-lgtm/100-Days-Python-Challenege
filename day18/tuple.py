# tuple
# creating tuple
my_tuple = (1, 2, 3)
# accessing and printing  the tuple
print(my_tuple[1])
# u can not change the value in tuple and u can not remove item from tuple
my_tuple[1] = 12
# we can really change the tuple into list by just writing
my_list = list(my_tuple)
for _ in range(3):
    print(my_list)
