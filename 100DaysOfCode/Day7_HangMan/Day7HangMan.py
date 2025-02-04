import random as rand
from stagesList import hangMan
from wordList import wordList

chosenWord = rand.choice(wordList)

placeholder = ' '.join(["_" for letter in chosenWord])

print(placeholder)

positions = placeholder.split()

lives = 6
gameOver = False
previous = list()

while not gameOver:

     print(f"Amount of lives: {lives}/6")

     guess = input("Guess a letter: ").lower()
     
     if guess in previous:
          print("You already guessed %s" %guess)

     elif guess in chosenWord:
          for i in range(len(chosenWord)):
               if chosenWord[i] == guess:
                    positions[i] = guess

          print(hangMan[lives])
          print(' '.join(positions))
        
          if '_' not in positions:
               print("You Win") 
               gameOver = True

     else:
          lives -= 1
          print(hangMan[lives])
          print(' '.join(positions) + "\n")
          print("You guessed %s and it's not in the word. You lose a life." %guess)
          if lives == 0:
               print(f"You Lose. The word was {chosenWord}.")
               gameOver = True
     previous.append(guess)
        
    
         
    

    
    