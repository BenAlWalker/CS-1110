# Ben Walker, baw3hg

import random

'''
This program lets the user take a specific amount of guesses
to guess a number. The computer tells the user if the current guess is
higher, lower, or the same as the solution.

'''

solution = int(input("What should the answer be? "))  # this is what the solution will be
guesscount = int(input("How many guesses? "))  # this is how many guesses the user gets

if solution == -1:  # if the user types -1, the solution will be a random integer from 1-10
    solution = random.randint(1, 1000)

while guesscount > 1:  # different outcomes if the amount of guesses is over 1
    numguess = int(input("Guess a number: "))
    if numguess == solution:
        print("You win!")
        break
    elif numguess < solution:
        print("The number is higher than that.")
        guesscount = guesscount - 1
    elif numguess > solution:
        print("The number is lower than that.")
        guesscount = guesscount - 1

if guesscount == 1:  # outcomes if the amount of guesses is equal to 1
    numguess = int(input("Guess a number: "))
    if numguess == solution:
        print("You win!")
    else:
        print("You lose; the number was", str(solution) + ".")
