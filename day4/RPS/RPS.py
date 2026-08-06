# ROCK PAPER SCISORSS GAME BUILT BY ME
import random

game = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""",
]
user_choice = int(
    input("What do you choose, Type 0 for rock, 1 for paper, 2 for scisors.\n")
)
if user_choice >= 0 and user_choice <= 2:
    print(game[user_choice])
    print("\n")
else:
    exit()
computer_choice = random.randint(0, 2)
print("Computer choice.\n")
print(computer_choice)
print(game[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("\nYou won! ")
elif user_choice == 2 and computer_choice == 0:
    print("\nYou lose! ")
elif user_choice > computer_choice:
    print("\nYou won! ")
elif computer_choice > user_choice:
    print("\nYou lose! ")
elif computer_choice == user_choice:
    print("It's a draw! ")
else:
    print("something went wrong. Game over\n")
