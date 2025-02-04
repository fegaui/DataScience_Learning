# Game for the user to guess who has more followers on instagram
from random import choice
import Game_data as gm
import Art
# use functions and try to wright as little code as possible

def compare(user_input, score, celebA, celebB):
    """Takes user input to compare if the user won the game
        returns score and result
    """
    if user_input == 'A' and celebA["follower_count"] > celebB["follower_count"]:
        score = score + 1
        return ['win', score]
         
    elif user_input ==  'B' and celebB["follower_count"] > celebA["follower_count"]:
        score = score + 1
        return ['win', score]
    else:
        return ['lose', score]

def choose_celeb():
    """returns a list with two random celebs from the data without repetition

    """
    celebs = [choice(gm.data), choice(gm.data)]

    while celebs[0] == celebs[1]:
        celebs[1] = choice(gm.data)
    
    return celebs

def show_game(celebA, celebB):
    """Shows the user the celebrities to compare"""
    print(f"Compare A: {celebA['name']}, a {celebA['description']}, from {celebA['country']}.")

    print(Art.vs)

    print(f"Against B: {celebB['name']}, a {celebB['description']}, from {celebB['country']}.")

def game():
    
    score = 0
    celebA = choose_celeb()[0]
    celebB = choose_celeb()[1]
    show_game(celebA, celebB)
    user_input = input("Who has more followers? 'A' or 'B': ")
    result = compare(user_input, score, celebA, celebB)[0]
    score  = compare(user_input, score, celebA, celebB)[1]

    while result == 'win':
        print(f"You're right! Current score: {score}")
        celebA = celebB
        celebB = choose_celeb()[0]
        show_game(celebA, celebB)
        user_input = input("Who has more followers? 'A' or 'B': ").capitalize()

        result = compare(user_input, score, celebA, celebB)[0]
        score  = compare(user_input, score, celebA, celebB)[1]
        
        
        
    print(f"Sorry that's wrong. Final score: {score}")

 
print(Art.logo)
game()



