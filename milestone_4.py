import random

class Hangman():
    def __init__(self, word_list, num_lives=5) -> None:
        self.word = random.choice(word_list)    # Word to be guessed, picked randomly from word_list.
        self.word_guessed = ['_'] * len(self.word)  # List of the letters of the word. '_' used for unguessed chars
        self.num_letters = len(set(self.word))  # Number of UNIQUE unguessed letters in the word. Created using sets
        self.num_lives = num_lives  # Number of lives at game start
        self.word_list = word_list  # List of words
        self.list_of_guesses = []   # List of already tried guesses. Initially empty

    def check_guess(self, guess):
        guess = guess.lower()

        # If the user guesses correctly
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, j in enumerate(self.word): # use the enumerate() function to loop over the word
                if j == guess:
                    self.word_guessed[i] = j    # Modify the word_guessed list with the character
            
            self.num_letters -= 1   # Reduce the num_letters variable by 1

        # If the user's guess is incorrect
        else:
            
            # Reduce the number of lives by 1
            self.num_lives -= 1

            # Prompt the user of an incorrect guess
            print(f"Sorry, {guess} is not in the word. Try again.")

            # Display number of remaining lives
            print(f"You have {self.num_lives} lives left.")

        self.list_of_guesses.append(guess)  # Append the guess to the list_of_guesses list

    def ask_for_input(self):
        while True:
            # Ask the user for input and assign to a variable called guess.
            guess = input('Guess a single letter: ')
            
            # Check that the guess is NOT a single, alphabetical character.
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Check if guess in list_of_guesses with elif statement
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            # For single alphabetical chars outside list_of_guesses
            else:
                self.check_guess(guess)
                # check_guess() function appends already -> line 37
                # self.list_of_guesses.append(guess)
                break

word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']

j = Hangman(word_list, 5)

j.ask_for_input()
print(j.list_of_guesses)