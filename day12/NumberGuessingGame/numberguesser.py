import random

logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \\
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""


def number_guessing_game():
    print(logo)
    print("Welcome To Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    guessing_number = random.randint(1, 100)
    # print(guessing_number)  # Uncomment for debugging

    Game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if Game_level == "easy" else 5
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        try:
            user_guess = int(input("Make a Guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess < guessing_number:
            print("Too Low.\nGuess Again!\n")
        elif user_guess > guessing_number:
            print("Too High.\nGuess Again!\n")
        else:
            print(f"You got it! The answer was {guessing_number}")
            return

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print(f"You've run out of guesses. The number was {guessing_number}.")


if __name__ == "__main__":
    number_guessing_game()
