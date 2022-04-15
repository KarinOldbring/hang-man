import random
from words import words

# generate valid random word

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word: 
        word = random.choice(words)
    
    return word

# Input username
name = input("What's your name?")
print(f"Good luck {name}!")