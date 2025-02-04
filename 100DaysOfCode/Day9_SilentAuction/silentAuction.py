def max_bid(dict):
    max = 0
    max_name = ""
    for name in bidders_dict:
        if bidders_dict[name] > max:
            max = bidders_dict[name]
            max_name = name
    print(f"The winner is {max_name} with a bid of ${max}.")



bidders_left = True
bidders_dict = {}

while bidders_left:
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?: $"))

    bidders_dict[name] = bid

    others = input("Are there other bidders? Type 'yes' or 'no'.\n").lower()
    if others == 'no':
        bidders_left = False
        print("\n"*100)
        max_bid(bidders_dict)
    



    

