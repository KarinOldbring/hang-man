import random
from words import words

""" 
generate valid randomm word
"""
def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word: 
        word = random.choice(words)
    
    return word