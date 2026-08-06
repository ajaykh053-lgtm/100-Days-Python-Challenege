# project on all we learnt


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of{highest_bid}.")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What's your name :")
    bid = int(input("What's your bet : $ "))
    bids[name] = bid
    another_bid = input("Is there anyone who wants to Bet! : 'yes'or 'no'\n").lower()
    print("\n" * 100)
    if another_bid == "no":
        continue_bidding = False
        find_highest_bidder(bids)
