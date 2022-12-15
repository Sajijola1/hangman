# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
The random module is the only python library required to run this programme

## Milestone 1

- The development environment for the project was set up. Github integration for the project was also configured
  
```python
"""Insert your code here"""
```

> Insert an image/screenshot of what you have built so far here.

## Milestone 2

- In this milestone, initial variables for the hangman game were created. The random module was imported. Lists were used for storing possible words while if-else statements were employed in logic flow of the program.

- The python file was executed as follows.

```bash
python3 milestone_2.py
```
## Milestone 3

- In this milestone, we defined functions in the programme, one to iteratively prompt the user for a valid guess and another to check if the user's guess is in the secret word. 

- As usual, the python file was executed using:

```bash
python3 milestone_3.py
```
## Milestone 4

- Here, object-oriented programming(OOP) conepts were employed to create a class for the hangman game. Functions from the previous milestone were integrated as methods of the class with new class atributes being defined to facilitate the flow of the game. These attributes were:

    - `word`: **string** The word to be guessed, picked randomly from the `word_list`. Remember to import the `random` module into your script.

    - `word_guessed`: **list** - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].

    - `num_letters`: **int** - The number of UNIQUE letters in the word that have not been guessed yet.

    - `num_lives`: **int** - The number of lives the player has at the start of the game.

    - `word_list`: **list** - A list of words.

    - `list_of_guesses`: **list** - A list of the guesses that have already been tried. Set this to an empty list initially.



The attributed defined for the class are shown in the screenshot below.

 ![alt text](ClassAttributes.png)

The functions defined in the previous milestone were encapsulated within the class as shown in the screenshot below, with behaviours being defined for both correct and incorrect user guesses.

![](ClassMethods1.png)


## Milestone 5

- In this milestone, we defined functions in the programme, one to iteratively prompt the user for a valid guess and another to check if the user's guess is in the secret word. 

- As usual, the python file was executed using:

```bash
python3 milestone_3.py
```

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
