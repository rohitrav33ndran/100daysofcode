#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo
print(logo)

print("I'm thinking of a number between 1 and 100")
randnum = random.randint(1,100)
difficulty = input("Choose a difficulty type 'easy' or 'hard' : ")


def checknumber(number):
    if number == randnum:
        return "win"
    elif number > randnum:
        return "Too high"
    else:
        return "Too low"

def play(guess_count):
    is_exit = False
    while guess_count > 0 and not is_exit:
        print(f"You got {guess_count} attempts remaining to guess the number")
        guess = int(input("Make a guess : "))
        result = checknumber(guess)
        guess_count -= 1
        if result == "win":
            print(f"You got it. The answer is {randnum}")
            is_exit = True
        else:
            print(result)
    if guess_count == 0:
        print("You have ran out of Guesses")
        print(f"The random number was {randnum}")

if difficulty == "hard":
    play(10)
else:
    play(5)



# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

