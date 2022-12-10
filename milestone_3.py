import random

word_list = ['bananas', 'apples', 'oranges', 'mangoes', 'blackberries']

word = random.choice(word_list)

while True:
    guess = input('Guess a single letter: ')
    
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")