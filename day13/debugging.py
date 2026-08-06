# Debugging Exercise
# def my_function():
#     for i in range(1,20):
#         if i==20:
#             print("You got it")
# corrected code
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Another debugging exercise
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_image=dice_imgs[randint(1,6)]
# print(dice_image)
# corrected code
from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
print(dice_images[randint(0, 5)])

# Debugging tips

# take a break
# ask a friend
# run often
# ask stack overflow\
# Target is the number up to which we count
