Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
Players = ["X", "O"]


def Print_Borad():
    print(f"{Board[0]} | {Board[1]} | {Board[2]}")
    print("----------")
    print(f"{Board[3]} | {Board[4]} | {Board[5]}")
    print("----------")
    print(f"{Board[6]} | {Board[7]} | {Board[8]}")


def is_player_win(Player):
    if Board[0] == Board[1] == Board[2] == Player:
        return "W"
    if Board[3] == Board[4] == Board[5] == Player:
        return "W"
    if Board[6] == Board[7] == Board[8] == Player:
        return "W"
    if Board[0] == Board[4] == Board[8] == Player:
        return "W"
    if Board[0] == Board[3] == Board[6] == Player:
        return "W"
    if Board[1] == Board[4] == Board[7] == Player:
        return "W"
    if Board[2] == Board[5] == Board[8] == Player:
        return "W"
    if Board[0] == Board[4] == Board[6] == Player:
        return "W"


def is_draw():
    draw = 0
    for i in Board:
        if i == "X" or i == "O":
            draw += 1
    return draw


def place(Input, Player):
    if Player == "X":
        Board[Input] = "X"
    else:
        Board[Input] = "O"


def valid_input(Input):
    if Board[Input] == "X" or Board[Input] == "O":
        return False
    elif Input is int:
        return True
    elif Input in range(len(Board)):
        return True
    else:
        return False


is_true = True
while is_true:
    Player1 = str(input("Choose One :- X or O : "))
    if Players.index(Player1) == 0:
        Player2 = Players[1]
    else:
        Player2 = Players[0]
    print("""
    ░██████████░██         ░██████████               ░██████████                 
        ░██                    ░██                       ░██                     
        ░██    ░██ ░███████    ░██ ░██████  ░███████     ░██ ░███████  ░███████  
        ░██    ░██░██    ░██   ░██      ░██░██    ░██    ░██░██    ░██░██    ░██ 
        ░██    ░██░██          ░██ ░███████░██           ░██░██    ░██░█████████ 
        ░██    ░██░██    ░██   ░██░██   ░██░██    ░██    ░██░██    ░██░██        
        ░██    ░██ ░███████    ░██ ░█████░██░███████     ░██ ░███████  ░███████""")
    print(f"Player1 is {Player1} and Player2 is {Player2}")
    Print_Borad()
    for i in range(len(Board)):
        if i % 2 == 0:
            Input = int(input(f"Player {Player2}  enter position : "))
            if Input == 0 and Input == 1:
                pass
            else:
                Input = Input - 1
            if valid_input(Input):
                place(Input, Player2)
                if is_player_win(Player2) == "W":
                    print(f"{Player2} Won .")
                    break
                elif is_draw() == 9:
                    print("It's Draw .")
                    break
            else:
                print("Your Input Is Invalid Please Enter Only Number From (1,9)\n\
                    And Do not Give Number where you or opponent is placed already.")
                break
            Print_Borad()
        else:
            Input = int(input(f"Player {Player1}  enter position : "))
            if Input == 0 and Input == 1:
                pass
            else:
                Input = Input - 1
            if valid_input(Input):
                place(Input, Player1)
                if is_player_win(Player1) == "W":
                    print(f"{Player1} Won .")
                    break
                elif is_draw() == 9:
                    print("It's Draw .")
                    break
            else:
                print("Your Input Is Invalid Please Enter Only Number From (1,9)\n\
                    And Do not Give Number where you or opponent is placed already.")
                break
            Print_Borad()
    Choice = str(input("Wanna Play Again ! (y or n) : ")).lower()
    if Choice != "y":
        is_true = False
    else:
        Board.clear()
        Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Players = ["X", "O"]
