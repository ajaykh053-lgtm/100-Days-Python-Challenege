from logo import logo, vs
from gamedata import data
import random


def format_data(account):
    # format the account data in printable format
    account_name = account["name"]
    account_profession = account["profession"]

    account_origin = account["origin"]
    return f"{account_name}, {account_profession}, {account_origin}"


print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    # getting random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    # getting the followers count of each account
    account_followers_a = account_a["followers_millions"]
    print(account_followers_a)
    account_followers_b = account_b["followers_millions"]
    print(account_followers_b)
    # printing the logo and the formatted account data

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n" * 20)

    def check_answer(user_guess, a_followers, b_followers):
        if a_followers > b_followers:
            return user_guess == "A"
        else:
            return user_guess == "B"

    is_correct = check_answer(guess, account_followers_a, account_followers_b)
    if is_correct:
        score += 1
        print(logo)
        print(f"You are right! Current score: {score}")
    else:
        print("\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
