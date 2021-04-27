import random
from words import words # File containing all the necessary words to play hangman
import string # Common string operations


def getValidWords(words):
    word = random.choice(words)
    while " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getValidWords(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 10

    # Getting a user input
    while len(wordLetters) > 0 and lives > 0:
        # Keeping track of the user input
        print("You have", lives, "lives left and you have used these letter : ", " ".join(usedLetters))
        
        # Keeping track of what the user has guessed from the chosen word
        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word : ", " ".join(wordList))

        userLetter = input("Guess a letter : ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives = lives - 1
                print("Letter is not in the word!")

        elif userLetter in usedLetters:
            print("You have already used that letter. Please try another one!")

        else:
            print("Invalid character. Please, try again!")

    if lives == 0:
        print("You died. Sorry, the word was : ", word)
    else:
        print("Congratulations. You have guessed the word : ", word)

hangman()