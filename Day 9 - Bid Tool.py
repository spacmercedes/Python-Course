


def find_highest_bidder(bidding_dict):
    highbid = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highbid:
            highbid = bid_amount
            winner = bidder
    print(f"Winner is {winner}")


bid_dict = {}
continuebid = True

while continuebid:
    name = input("Insert your name: ")
    bid = int(input("Add your bid: $"))

    bid_dict[name] = bid

    done_bid_inp = input("Are there any more bidders? ")

    if done_bid_inp == "no":
        continuebid = False
        find_highest_bidder(bid_dict)
    elif continuebid == "yes":
        print("\n" * 100)