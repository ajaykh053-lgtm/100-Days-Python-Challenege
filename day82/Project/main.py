## Text To Morse Code Converter.
from Convert_Morse_code import Morse_Code_Converter
from Morse_Code_Audio import play_morse

Morse_Code = Morse_Code_Converter()
wanna_continue = True
while wanna_continue:   
    choice = int(
        input(
            "Choose the option below (1 or 2) :\n1 -- > Text to Morse Code.\n2 --> Morse Code to Text.\n"
        )
    )
    if choice == 1:
        Text = str(
            input("Enter the text that you want to convert into Morse code :- ")
        ).upper()
        Morse = Morse_Code.Convert_to_code(Text=Text)
        print(Morse)
        Audio = input("Do you Want to hear the Morse Code (y or n) :- ").lower()
        if Audio == "y":
            play_morse(Morse)
        else:
            pass
        if input("Do you want to coontinue (y or n):\n") == "y":
            wanna_continue = True
        else:
            wanna_continue = False
    elif choice == 2:
        Code = str(input("Enter Morse Code that you want to convert into Text :- "))
        code_list = Code.split()
        # print(code_list)
        print(Morse_Code.Convert_to_text(Code_list=code_list))
        if input("Do you want to coontinue (y or n):\n") == "y":
            wanna_continue = True
        else:
            wanna_continue = False
    else:
        print("Please select the Available option")
        if input("Do you want to coontinue (y or n):\n") == "y":
            wanna_continue = True
        else:
            wanna_continue = False
