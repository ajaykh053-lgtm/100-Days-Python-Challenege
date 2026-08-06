def add(*Args):
    Sum = 0
    for Numbers in Args:
        Sum = Sum + Numbers
    return Sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))


# Unlimited Keyworded Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs["add"]
    n+=kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

# Quiz

# Question 1:
# What is the output of this code?
# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
# bar(1, 2)

# Answer = 1, 2, 'yes please!', 0

# Question 2:
# What is the output of this code?
# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
# bar(toast='nah', spam=4, eggs=2)

# Answer = 4, 2, 'nah', 0

# Question 3:
# def test(*args):
#     print(args)
# test(1,2,3,5)
# What is the data type of args?

# Answer = tuple

# Question 4:
# def test(*args):
#     print(args)
# test(1,2,3,5)
# What is the output of the code above?

# Answer = (1, 2, 3, 5)

# Question 5:
# def all_aboard(a, *args, **kw): 
#     print(a, args, kw)
# all_aboard(4, 7, 3, 0, x=10, y=64)
# What is the output of the code above? 

# Answer = 4 (7, 3, 0) {'x':10,'y':64}
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        # using get fun if the value 
        # donest exsist in kw it will return non
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car=Car(make="Nisaan",model="GTR")
