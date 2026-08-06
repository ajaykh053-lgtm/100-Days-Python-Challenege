# Defualt Agrguments Quiz
# Question 1:
# What is the output of this code?
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(1)
# Answer = 1,4,6

# Question 2:
# What is the output of this code?
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(4, 9)
# Answer = 4,9,6

# Question 3:
# What is the output of this code?
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(1, 7, 9)
# Answer = 1, 7, 9

# Question 4:
# What is the output of this code
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(20, c=6)
# Answer = 20, 4, 6


# Unlimited Positional Arguments
# Normal
def add(n1, n2):
    return n1 + n2

add(1, 2)

# add(n1=5, n2=3)#here we only give 2
# Unlimited
def add(*args):
    for n in args:
        print(n)


add(1, 2, 3, 4, 5)
from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(height=300, width=500)
window.config(padx=100, pady=100)


def button_Clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
# my_label.config(text="Button got clicked")# this is for previus exmaple
# my_label.pack(side="left")
# my_label["text"] = "New Text"

# my_label.pack()
my_label.place(x=100,y=200)
my_label.config(padx=50, pady=50)  # this is way to add padding to each item in window
my_label.grid(row=0, column=0)


# Button
clickme1 = Button(text="Click Me 1", command=button_Clicked)
clickme2 = Button(text="Click Me 2", command=button_Clicked)
# button.pack()
clickme1.grid(row=0, column=2)
clickme2.grid(row=1, column=3)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=1, row=0)

window.mainloop()
