import random
from words import words

# generate valid random word

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word: 
        word = random.choice(words)
    
    return word.upper()

# Input username
name = input("What's your name?")
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
    print("Guess the word by choosing a letter: " + " ".join(secret_word) +"\n")

play_game()