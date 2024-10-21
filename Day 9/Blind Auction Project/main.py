import art

print(art.logo)

# TODO-1: Ask the user for input
name = input("What is your name: ")
bid = int(input("What is your bid: $"))

# TODO-2: Save data into dictionary {name: price}
bids = {}
bids[name] = bid

# TODO-3: Whether if new bids need to be added
more = input("Are there any other bidders: ")
while more != "no":
    print("\n" * 20)
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    bids[name] = bid
    more = input("Are there any other bidders: ")

# TODO-4: Compare bids in dictionary
max_key = max(bids, key=bids.get)
print(f"The winner is {max_key} with a bid of ${bids[max_key]}")



