alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q","r","s","t","u","v","w","x","y","z"]

def caesar(direction, text, shift):
        output_text = ""
        if direction == "decode":
              shift *= -1
        for letter in text:
            if letter not in alphabet:
                output_text += letter
            else:
                output_text += alphabet[(alphabet.index(letter) + shift)%26]
        print(f"Here is the {direction} result: {output_text}")
    

gameOver = False

while not gameOver:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Enter shift number: \n"))

    caesar(direction, text, shift)
    
    again = input("Type 'Yes' if you want to go again. Otherwise type 'No': \n").lower()
    if again == 'yes':
          gameOver = False
    else:
          gameOver = True
          print("Goodbye broski")