# ...existing code...
import os
import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Takes list of cards and returns calculated score (0 means Blackjack)"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # convert one Ace (11) to 1 if bust
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🤐"
    if user_score == 0:
        return "You win with a Blackjack! 🤩"
    if computer_score == 0:
        return "You lose — opponent has Blackjack 🥲"
    if user_score > 21:
        return "You went over. You lose 🥲"
    if computer_score > 21:
        return "Opponent went over. You win 🤩"
    if user_score > computer_score:
        return "You win 😎"
    return "You lose 😒"


def play():
    print(
        """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
    |  \/ | /  \ |     | |_ | | (_| | (__|   <| | (_| | (__|   < 
    '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          '------'                           |__/       
    """
    )
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another = (
                input("Type 'y' to get another card, type 'n' to pass: ")
                .lower()
                .strip()
            )
            if another == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer final cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# ...existing code...

if __name__ == "__main__":
    while True:
        play_again = (
            input("Do you want to play Blackjack? Type 'y' or 'n': ").lower().strip()
        )
        if play_again == "y":
            # clear screen on Windows
            os.system("cls")
            play()
        else:
            break
