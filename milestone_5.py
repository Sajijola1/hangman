import random

class Hangman():
    def __init__(self, word_list:list, num_lives:int=5) -> None:
        """Initialise the attributes of the class
        The class object takes a list of words as
        string variables and an int for the number 
        of lives as parameters.
        All class attributes are defined as private
        This is to ensure ensure encapsulation and
        to protect from external access or modification"""

        # Word to be guessed, picked randomly from word_list.
        self.__word = random.choice(word_list)
        
        # List of the letters of the word. '_' used for unguessed chars
        self.__word_guessed = ['_'] * len(self.__word)
        
        # Number of UNIQUE unguessed letters in the word. Created using sets
        self._num_letters = len(set(self.__word))
        
        # Number of lives at game start
        self._num_lives = num_lives

        # List of words
        self.__word_list = word_list

        # List of already tried guesses. Initially empty
        self.__list_of_guesses = []

    def check_guess(self, guess: str) -> None:
        """Checks whether the letter guessed by the user is in the 
        secret word that was randomly chosen by the computer.
        For example, if the user guesses the letter "a" and the 
        secret word is "apple", then your code should check if 
        "a" is in "apple".
        This function takes the guessed letter as an 
        argument and checks if the letter is in the word
        Returns None"""
        
        # Convert the guessed letter into lower case
        guess = guess.lower()

        # Create an if statement that checks if the guess is in the word
        if guess in self.__word:
        # print a message saying "Good guess! {guess} is in the word."
        # format the string to show the actual guess.
            print(f"Good guess! {guess} is in the word.")
            
            # Get index and element pairs for each letter 
            # in the word using enumerate () and a for loop
            for idx, letter in enumerate(self.__word):
                # Compare each letter in the randomly chosen word
                # with the user's guess 
                if letter == guess:
                    # Modify the word_guessed list with the user's guess
                    self.__word_guessed[idx] = letter
            
            # Number of UNIQUE unguessed letters reduces by 1
            self._num_letters -= 1

        # If the user's guess is incorrect
        else:
            
            # Reduce the number of lives by 1
            self._num_lives -= 1

            # Prompt the user of an incorrect guess
            print(f"Sorry, {guess} is not in the word. Try again.")

            # Display number of remaining lives
            print(f"You have {self._num_lives} lives left.")

        self.__list_of_guesses.append(guess)  # Append the guess to the list_of_guesses list

    def ask_for_input(self) -> None:
        """Continuously asks the user for a letter and validates it.
        Takes no parameters,
        Returns none"""
        
        # Create a while loop and set the condition to True
        while True:
            # Ask the user for input and assign to a variable called guess.
            guess = input('Guess a single letter: ')
            
            # Check that the guess is NOT a single, alphabetical character.
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Check if guess in list_of_guesses with elif statement
            elif guess in self.__list_of_guesses:
                print("You already tried that letter!")

            # For single alphabetical chars outside list_of_guesses
            else:
                # Call the check_guess method
                self.check_guess(guess)
                
                # Since the guess passes the checks, break out of the loop
                break

def play_game(word_list: list):
    """Create a function that will run all the code to run the game as expected."""
    
    # Create an instance of the Hangman class, pass word_list and num_lives as arguments
    game = Hangman(word_list, 3)
    
    # Create a while loop and set the condition to True
    while True:
        
        # Check if the number of lives is 0
        if game._num_lives == 0:
            # Print a message saying 'You lost!'
            print('You lost!')
            # Game ends
            break
        
        # Check if the number of UNIQUE unguessed letters is greater than 0
        elif game._num_letters > 0:
            # Continue the game and keep asking the user for input
            game.ask_for_input()
        
        # Check if the `num_lives` is not 0 and the `num_letters` is not greater than 0
        else:
            # The user has won, Print a message saying 'Congratulations. You won the game!'
            print('Congratulations. You won the game!')
            # Game ends
            break



word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']

play_game(word_list)
