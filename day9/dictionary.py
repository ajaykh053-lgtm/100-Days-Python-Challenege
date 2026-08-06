# defing the dictionary
programming_dictionary = {
    "bug": "A problem in program ",
    "funcrion": " used repeat same thing several times ",
}
# printing whole dictionary wihtout using fro loop
print(programming_dictionary)
# printing one of them in dictionary
print(programming_dictionary["bug"])
# edititng the item in the dictionary
programming_dictionary["bug"] = (
    "Bug id defined as the Error in code that cause problem in execution of the program"
)
print(programming_dictionary["bug"])
print(programming_dictionary)
# adding a item to dictionary
programming_dictionary["loop"] = (
    "its used to repeat sevseral statement continuesly until the condition become false"
)
print(programming_dictionary)
# to print all of them we use for loop
for key in programming_dictionary:
    print(programming_dictionary[key])
# clearing all the elements in dictionary by creating empty dictionary wiht same name
programming_dictionary = {}
print(programming_dictionary)
