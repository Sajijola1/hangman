import random

word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']

class Hangman():
    def __init__(self, word_list, num_lives=5) -> None:
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, j in enumerate(self.word): # use the enumerate() function to loop over the word
                if j == guess:
                    self.word_guessed[i] = j
            
            self.num_letters -= 1   # Reduce the num_letters variable by 1

        else:
            
            # Reduce the number of lives by 1
            self.num_lives -= 1

            # Prompt the user of an incorrect guess
            print(f"Sorry, {guess} is not in the word. Try again.")

            # Display number of remaining lives
            print(f"You have {self.num_lives} lives left.")

        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input('Guess a single letter: ')
            
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)
                # self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    game = Hangman(word_list, 3)

    while True:
        
        # Check if the `num_lives` is 0
        if game.num_lives == 0:
            # Print a message saying 'You lost!'
            print('You lost!')
            break
        
        # Check if the `num_letters` variable is greater than 0
        elif game.num_letters > 0:
            # Continue the game and call ask_for_input()
            game.ask_for_input()
        
        # Check if the `num_lives` is not 0 and the `num_letters` is not greater than 0
        else:
            # The user has won, Print a message saying 'Congratulations. You won the game!'
            print('Congratulations. You won the game!')
            break

play_game(word_list)

# j = Hangman(word_list, 5)

# j.ask_for_input()
# print(j.list_of_guesses)