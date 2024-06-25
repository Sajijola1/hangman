import random

# Create a list containing the names of your 5 favorite fruits
word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']

# Print the list to the screen
print(word_list)

# Call the random.choice method and pass the word_list variable into the choice method
# Assign the randomly generated word to a variable called word
word = random.choice(word_list)

# Print the word to the standard output
print(word)

# Using the input function, ask the user to enter a single letter.
# Assign the input to a variable called guess
guess = input('Please enter a single letter: ')

# Check if the length of the input is equal to 1 
# And the input is alphabetical
if len(guess) == 1 and guess.isalpha():
    # print a message that says "Good guess!"
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

