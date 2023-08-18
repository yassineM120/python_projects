#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import number_guessing_logo
import random

print(number_guessing_logo+"\n")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guessing_number = random.randrange(1,101)

print(f"developer cheat {guessing_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
game_end = False
easy_mode = 10
hard_mode = 5

while not game_end:
    if difficulty == "easy":
        print(f"You have {easy_mode} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == guessing_number:
            print(f"You got it! The answer was {guess}.")
            game_end = True
        else:
            if guess > guessing_number:
                print("Too high.")
            if guess < guessing_number:
                print("Too low.")
            easy_mode -= 1
    elif difficulty == "hard":
        print(f"You have {hard_mode} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        if guess == guessing_number:
            print(f"You got it! The answer was {guess}.")
            game_end = True
        else:
            if guessing_number - guess < 10:
                print("Too low.")
            else:
                print("Too high.")
            hard_mode -= 1
    if easy_mode == 0 or hard_mode == 0:
        game_end = True
        print("You've run out of guesses, you lose.")
