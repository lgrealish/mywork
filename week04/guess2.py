# guess1.py
# Author: Linda Grealish
# Prompts the user to guess a number and continutes
# to prompt until the user gets the correct number
# week 4 lab 2

numberToGuess = 78

guess = int(input ("Please guess the number : "))

while guess != numberToGuess:
    print ("Wrong")
    if (guess > numberToGuess):
        print ("Too high")
    if (guess < numberToGuess):
        print ("Too low")
    guess = int(input ("Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)