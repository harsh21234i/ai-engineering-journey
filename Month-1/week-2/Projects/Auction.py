import art

print(art.logo)

bids = {}

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


should_continue = "y"

while should_continue == "y":
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid price?: $"))

    bids[name] = bid_price

    should_continue = input(
        "Are there any other bidders? Type 'y' or 'n': "
    ).lower()


find_highest_bidder(bids)