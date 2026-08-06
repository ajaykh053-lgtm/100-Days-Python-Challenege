# function without parameters
def greet():
    print("Hello")
    print("How do youd do")
    print("Isn't the weather is nice?")


# greet()


# function witht input
def greeting_wiht_name(name):  # paameter
    print(f"Hello {name}")
    print(f"How do youd do {name}")


greeting_wiht_name("ajay")
greeting_wiht_name(123)  # arguments
greeting_wiht_name(1.0)
greeting_wiht_name("vishwa")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How's the weather in {location}")


# Calling greet_with() with Positional Arguments

greet_with("Jack Bauer", "Nowhere")

# vs.

greet_with("Nowhere", "Jack Bauer")


# Calling greet_with() with Keyword Arguments
greet_with(location="Wonda", name="Luffy")  # better one
