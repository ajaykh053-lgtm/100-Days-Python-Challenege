# # Functions can have inputs
# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# # Function can have other function as input
# def calculte(cal_func, n1, n2):
#     return cal_func(n1, n2)


# result = calculte(multiply, 2, 3)
# print(result)


# # Nested function
# def outer_function():
#     print("I'm outer")

#     def nested_fintion():
#         print("I'm inner")

#     return nested_fintion


# # Functions can be returned from other function
# inner_function = outer_function()
# inner_function()


# Python Decorator
# Decorater is function which takes the other function as input
# and wrap that functio in wrapper function and returns the wrapper function
def decorator_finction(function):
    def wrapper_function():
        print(
            "Adding Additional Fuctionalities to the exsisting function using decorator"
        )
        function()
        print("Ajay")

    return wrapper_function


@decorator_finction
def say_hi():
    print("hi")


say_hi()
