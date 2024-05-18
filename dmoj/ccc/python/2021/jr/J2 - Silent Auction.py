bids = int(input())
highest_bid = 0
highest_bidder = ''

for i in range(bids):
    name = input()
    bid_amt = int(input())
    if bid_amt > highest_bid:
        highest_bid = bid_amt
        highest_bidder = name
print(highest_bidder)
