import random as rd
    
def game(difficulty):
    lifes = 0

    if difficulty == "easy":
        lifes = 10
    elif difficulty == "hard":
        lifes = 5
    else:
        print("Invalid input")
    
    random_number = rd.randrange(1, 100)
    while lifes > 0:
        print(f"You have {lifes} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
        elif guess > random_number:
            print("Too high, guess again.")
            lifes = lifes - 1
        else:
            print("Too low, guess again.")
            lifes = lifes - 1
    print("You've run  out of guesses.")
    
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type'easy' or 'hard': ")

game(difficulty)