bids = {}

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
            
    print(f"The Winner is {winner} with a bid ${highest_bid}")

continue_bids = True
while continue_bids:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    print("\x1b[2J\033[H")
    more_user = input("Are there any other biders? Types 'yes' or 'no'\n")
    if more_user == 'no':
        continue_bids = False
        #find_highest_bidder(bids)
        winner = max(bids, key=bids.get)
        bid = bids[winner]
        print(f"The Winner is {winner} with a bid ${bid}")




