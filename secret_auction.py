from replit import clear
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
#creating a empty dictionary
mydict = {}

#making bidding process false initially
bidding = False

 #function for highest bid entered by user
def highest_bidder(bidder_record):
    highest = 0
    winner = ""

    #looping through mydict
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid amount ${highest}.")

#when bidding is not on process 
while not bidding:
    #input from user
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    #storing inputs in dcitionary
    mydict[name]=bid

    #for multiple bidders input
    ask = input("Are there other persons to bid? type yes or no:\n").lower()
    if ask == "no":
       #if not then final result will print
       bidding = True
       highest_bidder(mydict)
    elif ask == "yes":
        #importing clear function from replit module to clear the console after input of first user.
        clear()


   

