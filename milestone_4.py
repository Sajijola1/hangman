import random

class Hangman():
    def __init__(self, word_list, num_lives=5) -> None:
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = set(self.word) # Using the set() function to convert the word to a set of unique characters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []