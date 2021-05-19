import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rockpaperscissor=[rock, paper, scissors]
personchoice = int(input("Input your choice 0 - Rock, 1 - Paper, 2 - Scissors \n"))

if personchoice >=3 or personchoice < 0:
  print("Invalid Choice. You Lose")
else:
  print(rockpaperscissor[personchoice])
  computerchoice = random.randint(0,2)
  print("Computer chose \n")
  print(rockpaperscissor[computerchoice])


if personchoice == "0" and computerchoice == 2:
  print("You win")
elif computerchoice == "0" and personchoice == 2:
  print("You Lose")
elif personchoice > computerchoice:
  print("You win")
elif computerchoice > personchoice:
  print("You Lose")
elif personchoice == computerchoice:
  print("Play Again")
