from replit import clear

bid_list = []
answer = "yes"
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

while answer == "yes":
    name = input("What is your name ?: ")
    bid = input("What's your bid ?: ")
    bid_list.append({"name": name, "bid": bid})
    answer = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if answer == "no":
        answer = "no"
        winner_name = ""
        winner_bid = 0
        for bidders in bid_list:
            if int(bidders["bid"]) > int(winner_bid):
                winner_bid = bidders["bid"]
                winner_name = bidders["name"]
        print(f"The winner is {winner_name} with a bid of ${winner_bid}")
    else:
        clear()
