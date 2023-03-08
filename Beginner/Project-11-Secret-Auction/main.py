from logo import logo

print(logo)

- Clear Function is now a function that prints 50 blank spaces before the name of the next person that bids

bids = {}
bidding_finish = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    #bidding_record = {"Laura: 123, "James": 200}
    for bidder in bidding_record:
       bid_amount = bidding_record[bidder]
       if bid_amount > highest_bid:
           highest_bid= bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}" )
while not bidding_finish:
    name = input("What is your name?")
    price  = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes'or 'not'" )
    if should_continue == "not":
      bidding_finish = True
      find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

