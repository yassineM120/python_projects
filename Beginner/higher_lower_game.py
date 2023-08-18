from art import higher_lower_game_logo , vs
from game_data import data
import random
import os
def game_picks():
    first_choice = data[random.randint(0, len(data) - 1)]
    second_choice = data[random.randint(0, len(data) - 1)]
    if first_choice == second_choice:
        second_choice = data[random.randint(0, len(data) - 1)]
    return first_choice, second_choice
def game_prints(first,second):
    print(higher_lower_game_logo+"\n")
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.\n")
    print(vs+"\n")
    print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}.\n")

game_prints(game_picks()[0],game_picks()[1])
score = 0
game_end = False

while not game_end:
    player_pick = input("Who has more followers? Type 'A' or 'B': ").lower()
    fist_choice_score = game_picks()[0]['follower_count']
    second_choice_score = game_picks()[1]['follower_count']
    if player_pick == "a":
        if fist_choice_score > second_choice_score:
            os.system('cls')
            score +=1
            print(f"You're right! Current score: {score}.")
            game_prints(game_picks()[0], game_picks()[1])
        else:
            game_end = True
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        if fist_choice_score < second_choice_score:
            os.system('cls')
            score += 1
            print(f"You're right! Current score: {score}.")
            game_prints(game_picks()[0], game_picks()[1])
        else:
            game_end = True
            print(f"Sorry, that's wrong. Final score: {score}")



