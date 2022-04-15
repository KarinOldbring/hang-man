import random
from words import words

# generate valid random word

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word: 
        word = random.choice(words)
    
    return word.upper()

# Input username
name = input("What's your name?\n")
print(f"Good luck {name}!")

turns = 6

def play_game():
    word = get_valid_word(words)
    secret_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    turns = 6
    print("Let's start!")
    print(f"Turns left: {turns}")
    print("Secret word: " + " ".join(secret_word) +"\n")

    while not guessed and turns > 0:
        guess = input("Guess a letter: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already tried {guess}, try again")
            elif guess not in secret_word:
                print(f"Sorry, {guess} is not in the word")
                turns -= 1
                guessed_letters.append(guess)
                print(f"You have {turns} tries left.")
            else:
                print(f"Well done, {guess} is in the word!")
            
        else: 
            print(f"{guess} is not a valid guess, please choose a letter")

   
        

play_game()