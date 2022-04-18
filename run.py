import random
from words import words
import string

print("Hi! Let's play Hangman!")

# generate valid random word

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

# Input username
name = input("What's your name?\n")
print("Good luck", name, "!")

turns = 6

def play_game():
    alpha = set(string.ascii_uppercase)
    word = get_valid_word(words)
    letters_word = set(word)
    secret_word = "_" * len(word)
    guessed = False
    guessed_letters = set()
    guessed_words = set(word)
    turns = 15
    print("Let's start!")
    print("Turns left: ", turns)
    print(secret_word)
    #print("Secret word: " + " ".join(secret_word) +"\n")

    while len(letters_word) and turns > 0:

        letter_list = [letter if letter in guessed_letters else "_" for letter in word]
        print(" Guessed letters: ", " ".join(guessed_letters))
        print("Turns left: ", turns)
        guess = input("Pick a letter: \n").upper()

        #valid choice
        if guess in alpha - guessed_letters:
            guessed_letters.add(guess)
            if guess in letters_word:
                letters_word.remove(guess)
                print("" "Well done!")

            else:
                turns -= 1
                print(guess, "is not in the secret word, try again")
        
        elif guess in guessed_letters:
            print("You already tried", guess, ", try again")
        
        else:
            print(guess, "is not a valid guess, please choose one letter")
    
        for letter in word:
            if letter in guessed_letters:
                print(letter, end="")
            else: 
                print(" _ ", end="")

    if turns == 0:
        print("Sorry you lost, the secret word was", word)
    else:
        print(" Congratulations! The secret word was", word)

   
        

play_game()