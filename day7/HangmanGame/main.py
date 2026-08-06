import random
from hangman_word import word_list
from hangman_art import stages

lifes = 3
# choosing random word from word list

choosen_word = random.choice(word_list)
choosen_word_length = len(choosen_word)
# printing same number of blanks as choosen word

placeholder = ""
for i in range(choosen_word_length):
    placeholder += "_"

print("""
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       """
)
print(f"Word to guess : {placeholder}")
# filling the blanks wiht looping statements

game_over = False
correct_letters = []

while not game_over:
    guess = input("guess a word : ")
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in choosen_word:
        lifes -= 1
        if lifes == 0:
            game_over = True
            print("you lose")

    if "_" not in display:
        game_over = True
        print("you won")

    print(stages[lifes])
