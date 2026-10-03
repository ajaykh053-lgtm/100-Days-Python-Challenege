from Morse_Code_Dict import MORSE_CODE_DICT, REVERSED_MORSE_CODE_DICT


class Morse_Code_Converter:
    def __init__(self):
        self.Morse_Code = ""
        self.Text = ""

    def Convert_to_code(self, Text):
        for letter in range(len(Text)):
            # print(Text[letter])
            if Text[letter] == " ":
                # print(' / ')
                self.Morse_Code = self.Morse_Code + " / "
            elif Text[letter] in MORSE_CODE_DICT:
                # print(' Letter Exsist in dict ')
                self.Morse_Code = self.Morse_Code + f" {MORSE_CODE_DICT[Text[letter]]} "
            else:
                print(f"Morse Code Not exsist for {Text[letter]}")
        return self.Morse_Code

    def Convert_to_text(self, Code_list):
        for Symbol in Code_list:
            # print(Symbol)
            if Symbol == "/":
                # print(' ')
                self.Text = self.Text + " "
            elif Symbol in REVERSED_MORSE_CODE_DICT:
                # print(' Letter Exsist in dict ')
                self.Text = self.Text + f"{REVERSED_MORSE_CODE_DICT[Symbol]}"
            else:
                print(f"Text Not exsist for {[Symbol]}")
        return self.Text.title()
