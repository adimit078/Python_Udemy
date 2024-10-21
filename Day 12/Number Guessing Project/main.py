import random
from random import randint

print("Welcome")

#Random number
number = random.randint(1,100)
easyMode = True if (input("Easy or hard: ").lower() == "easy") else False

#Returns -1 if number is less, 0 if number is more, and 1 if correct
def gradeGuess(guess):
    if (number < guess):
        return -1
    elif (number > guess):
        return 0
    elif (number == guess):
        return 0

guessesLeft = 0

if (easyMode):
    guessesLeft = 10
else:
    guessesLeft = 5

correct = False
while correct == False and guessesLeft > 0:
    print(f"You have {guessesLeft} to guess the number.")
    guess = int(input("Make a guess: "))
    result = gradeGuess(guess)

    if result == -1:
        print("Too high")
        guessesLeft -= 1
    elif result == 0:
        print("Too low")
        guessesLeft-=1
    elif result == 1:
        print("Correct!!")
        correct = True




