import random


word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']


print(word_list) 

word = random.choice(word_list)


print(word) 

def check_guess(char):
    """This function takes the guessed letter as an argument 
    and checks if that letter is in the secret word."""
    
    
    char = char.lower()
    
    
    if char in word:
        print(f"Good guess! {char} is in the word.")
    else:
        print(f"Sorry, {char} is not in the word. Try again.")

def ask_for_input():
    """Asks the user for input and iteratively checks to see 
    if the input is a valid guess"""
    while True:
        
        guess = input('Guess a single letter: ')
        
        
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    
    check_guess(guess)


ask_for_input()