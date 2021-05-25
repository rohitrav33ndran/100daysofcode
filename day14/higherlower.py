from replit import clear
from game_data import data
from art import logo
from art import vs
import random


count = 0
print(logo)

#need a method to get a random item from list of dictonaries
def getRandomItem():
    return random.choice(data)

#need a method to compare the follower_count
def compareFollowerCount(A,B):
    for k,v in A.items():
        if k == "follower_count":
            A_follower_count = v
    for k,v in B.items():
        if k == "follower_count":
            B_follower_count = v
    if A_follower_count > B_follower_count:
        return "A"
    else:
        return "B"

#Method to print the item in format
#Compare A: Cristiano Ronaldo, a foot_baller, From portugal
def printItem(item):
    for k,v in item.items():
        if k == "name":
            name = v
        if k == "description":
            description = v
        if k == "country":
            country = v
    fstring = f": {name}, {description}, from {country}"
    return fstring 
 

A = getRandomItem()

is_exit = False
while len(data) == 0 or not is_exit:
    #Print the random item in format
    aout = printItem(A)
    print(f"Compare A: {aout}")
    #Print the VS logo 
    print(vs)
    # Get a random item again 
    # Save the random item as B
    B = getRandomItem()
    # Print the random item in format  
    bout = printItem(B)
    print(f"Compare B: {bout}")
    #compare the follower count
    result = compareFollowerCount(A,B)
    userinput = input("who has more followers? Type A or B : ")
    #if user input matches the comparison value
    if userinput == result:
        count += 1
        if userinput == "B":
            A = B
    else:
        is_exit = True
        clear()
        print(logo)
        print(f"Sorry you got it wrong. Your final score is {count}")  

