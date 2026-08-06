# # if we just imported turtle module
# import turtle

# tim=turtle.Turtle()#this is how wee need to.
#                    # create object for Turtle class


# if we  imported turtle module like
# from turtle import Turtle
# # here we dont need write eevry time tutrtle.Turte() just write4
# tim=Turtle()
# ton=Turtle()
# tory=Turtle()

# there is another way from you can imprt everthiny in hat module
# from turtle import *

import turtle as t

import heroes  # type: ignore

print(heroes.gen())
