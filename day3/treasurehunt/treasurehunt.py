print(
    '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]'''
)

print("welcome to treasure Island.")
print("Your misiion is to find the treasure.")
choice1 = input(
    'you are at a crossroad, where do you want to go? type "left" or "rigth" \n'
).lower()
if choice1 == "left":
    choice2 = input(
        "you have came to lake. There is island in the middle of the lake . "
        'Type "wait" to wwaut for a boat. Type "swim" to swim across \n'
    ).lower()
    if choice2 == "wait":
        choice3 = input(
            "you are in front of 3 doors with 3 colours choose one get the treasure."
            "choose red , yellow , bule \n"
        ).lower()
        if choice3 == "bule":
            print("You won . you got thw treasure one peice")
        elif choice3 == "yellow":
            print("you got killed by crocodile . Game over ")
        elif choice3 == "red":
            print("you entered room wiht full of fire your died . Game over ")
    else:
        print("you are etaen by the shark . Game over")
else:
    print("you fell into wollpool. Game over")
