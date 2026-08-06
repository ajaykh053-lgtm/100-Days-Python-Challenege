# Exceptoin Handleing .
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sfdfsd"])
except FileNotFoundError:
    file = open("data.txt", mode="w")
    file.write("Something...")
except KeyError as error_message:
    print(f"The kry {error_message} does not exsist .")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file is closed .")
    a_dictionary.clear()
    print("dictinary is clear .")


# Raising our own exceptions .

# using raise keyword

height = float(input("Height : "))
weight = int(input("Weight : "))

if height > 3:
    raise ValueError("A Human height should not over 3 3 meters .")

BMI = weight / height**2
print(BMI)


#Index Error Handling

fruits = ["Apple", "Pear", "Orange"]

    # Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError :
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)
