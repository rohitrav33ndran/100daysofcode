from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
print("Welcome to the secret auction program")

is_exit = False
is_next_bid = True

while not is_exit:
  bidders = {}
  while is_next_bid:
    name = input("What's is your name. ? : ")
    bid = int(input("What is your bid. ? : $"))
    bidders[name] = bid

    nextbid = input("Are there any more bidders. Type yes or no : ").lower()
    clear()
    if nextbid == "yes":
      is_next_bid = True
    else:
      is_next_bid = False

  maxbid=0
  winner=""
  for name,bid in bidders.items():
    if bid > maxbid:
      maxbid = bid
      winner = name
  print(f"The winner is {winner} with a bid of ${maxbid}")
  is_exit = True
  
