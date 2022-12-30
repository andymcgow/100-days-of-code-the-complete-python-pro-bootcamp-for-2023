#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")

NUMBER = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")
# Print correct number for debugging.
# print(f"Pssst, the correct number is {NUMBER}.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

LIVES = 0

if difficulty == "easy":
    LIVES = 10
elif difficulty == "hard":
    LIVES = 5

def guessing():
    global NUMBER
    global LIVES
   
    guess = 0
    
    while LIVES >= 1:
        print(f"You have {LIVES} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == NUMBER:
            return print(f"You got it! The answer was {NUMBER}.")
        elif guess > NUMBER:
            print("Too high.")
            LIVES -= 1
            if LIVES >= 1:
                print("Guess again.")
        elif guess < NUMBER:
            print("Too low.")
            LIVES -= 1
            if LIVES >= 1:
                print("Guess again.")

    if LIVES == 0:
            return print("You've run out of guesses, you loose.")

guessing()