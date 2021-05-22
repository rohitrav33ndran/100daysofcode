import random
import hangman_art
import hangman_words

stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
chosen_word_length = len(chosen_word)
for _ in range(chosen_word_length):
  display += "_"

end_game = False
lives = 6

while not end_game:
  
    guess = input("Guess a letter in the chosen word : ").lower()
    for position in range(chosen_word_length):
      letter = chosen_word[position]
      if letter == guess:
        if letter not in display:
          print(f"You chose a letter '{guess}' which is present in the chosen word")
          display[position]=letter
          print(display)
        else:
          print(f"You have already guessed the letter {guess}")
          print(display)

    if guess not in chosen_word:
      print(f"You guess a letter '{guess}' which is not in the chosen word. You lose a life.")
      lives -= 1
      print(display)
      if lives == 0:
        end_game = True
        print("You Lose")

    if display.count("_") == 0:
      end_game = True
      print("You Win")

    print(stages[lives])
