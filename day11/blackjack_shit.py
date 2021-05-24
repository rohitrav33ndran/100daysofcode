import art
import random
from replit import clear

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player = {}
computer = {}
player_score = 0
computer_score = 0

def calculate_score(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum

def blackjack(player_score, computer_score):
    if player_score == 21 or computer_score == 21:
        return True
    else:
        return False

def player_play(player_cards):
    player.pop("score")
    player_cards.append(random.choice(cards))
    player_score = calculate_score(player_cards)
    player["score"] = player_score
    #print(f"player_play : {player}")
    return player

def computer_play(computer_cards):
    computer.pop("score")
    computer_cards.append(random.choice(cards))
    computer_score = calculate_score(computer_cards)
    computer["score"] = computer_score
    #print(f"computer_play : {computer}")
    return computer

def get_Cards_and_Score(user):
    for key,value in user.items():
        if key == "cards":
            user_cards = value
        else:
            user_score = value
    
    return user_cards,user_score

def draw_anothercard(user,check_player):
    if check_player == "player":
        player_cards,player_score = get_Cards_and_Score(user)
        player = player_play(player_cards)
        return player
    else:
        computer_cards,computer_score = get_Cards_and_Score(user)
        computer = computer_play(computer_cards)
        return computer

def user_played_next(player,computer):
    is_blackjack = blackjack(player_score, computer_score)
    if is_blackjack:
        print(f"Your cards {player_cards}. Current score is {player_score}")
        print(f"Computer cards {computer_cards}. Computer score is {computer_score}")
        print("You Win")
        return True
    else:
        if player_score > 21:
            if 11 not in player_cards:
                print("You Lose")
                print(f"Your cards {player_cards}. Current score is {player_score}")
                print(f"Computer cards {computer_cards}. Computer score is {computer_score}")
                return False
            else:
                print(player)
                if player_score - 10 > 21:
                    print("You lose")
                    print(f"Your cards {player_cards}. Current score is {player_score}")
                    print(f"Computer cards {computer_cards}. Computer score is {computer_score}")
                    return False
                else:
                    play_next = input("Type 'y' to get another card, type 'n' to pass:").lower()
                    if play_next == "y":
                        player = draw_anothercard(player,"player")                       
                    else:
                        print("no card")
        else:
            #print(player)
            play_next = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if play_next == "y":
                player = draw_anothercard(player,"player")              
            else:
                print("no card")

clear()
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
print(art.logo)
is_player_wins = False

player_cards = random.choices(cards,k=2)
player_score = calculate_score(player_cards)
player["cards"] = player_cards
player["score"] = player_score


computer_cards = random.choices(cards,k=2)
computer_score = calculate_score(computer_cards)
computer["cards"] = computer_cards
computer["score"] = computer_score

print(f"Your cards {player_cards}. Current score is {player_score}")
print(f"Computers cards : {len(computer_cards)}")

is_exit = False
is_user_draw_anothercard = True
while is_user_draw_anothercard:
    
    if not is_exit:
        result = user_played_next(player,computer)
        if result == True:
            
        if computer_score < 17:
            computer = draw_anothercard(computer,"computer")
            computer_cards,computer_score = get_Cards_and_Score(computer)
            if computer_score > 21:
                print("You Win")
                print(f"Your cards {player_cards}. Current score is {player_score}")
                print(f"Computer cards {computer_cards}. Computer score is {computer_score}")
            else:
                player_cards,player_score = get_Cards_and_Score(player)
                if player_score > computer_score:
                    print("You Win")
                    print(f"Your cards {player_cards}. Current score is {player_score}")
                    print(f"Computer cards {computer_cards}. Computer score is {computer_score}")
                elif computer_score > player_score:
                    print("You Lose")
                    print(f"Your cards {player_cards}. Current score is {player_score}")
                    print(f"Computer cards {computer_cards}. Computer score is {computer_score}")
                else:
                    print("Draw")
                    print(f"Your cards {player_cards}. Current score is {player_score}")
                    print(f"Computer cards {computer_cards}. Computer score is {computer_score}")
    else:
        is_user_draw_anothercard = False

