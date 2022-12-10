import random

# Store the possible words in a python list
word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']

# Prints the list of words
print(word_list) 

word = random.choice(word_list)

# Prints the secret word
print(word) 

def check_guess(char):
    """This function takes the guessed letter as an argument 
    and checks if that letter is in the secret word."""
    
    # Converts the guess into lower case
    char = char.lower()
    
    # Checks to see if the guess is in the specified word
    if char in word:
        print(f"Good guess! {char} is in the word.")
    else:
        print(f"Sorry, {char} is not in the word. Try again.")

def ask_for_input():
    """Asks the user for input and iteratively checks to see 
    if the input is a valid guess"""
    while True:
        # Query the user for input
        guess = input('Guess a single letter: ')
        
        # Check for valid entry
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    # Call the check_guess function
    check_guess(guess)

# Call the ask_for_input function
ask_for_input()