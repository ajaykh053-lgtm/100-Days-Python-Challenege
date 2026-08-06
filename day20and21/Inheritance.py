#Syntax
class Animal:
    def __init__(self):
        self.numm_eyes=2
    def breath(self):
        print("Inhale, Exhale")
class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breath(self):
        super().breath()
        print("Doing this underwater")
    def Swim(self):
        print("Moving in water")

nemo=Fish()
nemo.Swim()
nemo.breath()
print(nemo.numm_eyes)

#List slicing

piano_keys=["a","b","c","d","e","f","g"]
print(piano_keys[2:5])#slipt from 2 inex to 5 index
print(piano_keys[1:])#slipt from index 1 to everything in it
print(piano_keys[:5])#slipt fom startig to 5 th index
print(piano_keys[::2])#prints you except the second position in list like except even index
print(piano_keys[::-1])#reverse the list
piano_tuple=("a","b","c","d","e","f","g")
print(piano_tuple[2:5])#slipt from 2 inex to 5 index
print(piano_tuple[1:])#slipt from index 1 to everything in it
print(piano_tuple[:5])#slipt fom startig to 5 th index
print(piano_tuple[::2])#prints you except the second position in tuple like except even index
print(piano_tuple[::-1])#reverse the tuple

            
