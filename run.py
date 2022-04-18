import random
from words import words
import string

print("Hi! Let's play Hangman!")

# Generate valid random word

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

# Input username
name = input("What's your name?\n")
print("Good luck", name, "!")

# Play game
def play_game():
    alpha = set(string.ascii_uppercase)
    word = get_valid_word(words)
    letters_word = set(word)
    secret_word = "_" * len(word)
    #guessed = False
    guessed_letters = set()
    guessed_words = set(word)
    turns = 6
    print("Let's start!")
    print(stages_for_hanging(turns))
    print("Turns left: ", turns)
    print(secret_word)

    # While loop for the game to run
    while len(letters_word) and turns > 0:

        print(" Guessed letters: ", " ".join(guessed_letters))
        print("Turns left: ", turns)
        guess = input("Pick a letter: \n").upper()

        # Valid choice
        if guess in alpha - guessed_letters:
            guessed_letters.add(guess)
            if guess in letters_word:
                letters_word.remove(guess)
                print("" "Well done!")

            else:
                turns -= 1
                print(guess, "is not in the secret word")
        
        # If user picks the same letter
        elif guess in guessed_letters:
            print("You already tried", guess, ", try again")
        
        # Unvalid enter
        else:
            print(guess, "is not a valid guess, please choose one letter")
    
        # Show letters in secret word
        for letter in word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print(" _ ", end="")

    # If player runs out of turns
    if turns == 0:
        print(" Sorry you lost, the secret word was", word)
    # If player guesses the right word
    else:
        print(" Congratulations! The secret word was", word)

def stages_for_hanging(turns):
    stages = [  # final stage: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[turns]

   
        

play_game()