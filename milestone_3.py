import random

word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']

word = random.choice(word_list)

def check_guess(guess:str) -> None:
    """Checks whether the letter guessed by the user is in the 
    secret word that was randomly chosen by the computer.
    For example, if the user guesses the letter "a" and the 
    secret word is "apple", then your code should check if 
    "a" is in "apple".
    This function takes the guessed letter as an 
    argument and checks if the letter is in the word"""
    
    # Convert the guess into lower case
    guess = guess.lower()
    
    # Create an if statement that checks if the guess is in the word
    if guess in word:
        # print a message saying "Good guess! {guess} is in the word."
        # format the string to show the actual guess.
        print(f"Good guess! {guess} is in the word.")
    else:
        # Print a message saying 
        # "Sorry, {guess} is not in the word. Try again."
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input() -> None:
    """Write code that will continuously ask the user for 
    a letter and validate it."""
    
    # Create a while loop and set the condition to True
    while True:
        # Ask the user to guess a letter 
        # Assign this to a variable called guess
        guess = input('Guess a single letter: ')
        
        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            # If the guess passes the checks, break out of the loop
            break
        else:
            # If the guess does not pass the checks print a message to the screen
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    # Call the check_guess function to check 
    # if the guess is in the word
    check_guess(guess)

# Call the ask_for_input function
ask_for_input()