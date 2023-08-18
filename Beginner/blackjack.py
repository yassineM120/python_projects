from art import blackjack_logo
import random
import os

def calculat_score(list):
    score = 0
    for scores in list:
        score += int(scores)
    return score

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_ace(list):
    for score in list:
        if score == 11 and calculat_score(list) > 21:
            list[score] = 1


def blackjack(game):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    bot_hand = []
    player_score = 0
    bot_score = 0
    game_end = game
    while not game_end:
        first_card = int(random.choice(cards))
        second_card = int(random.choice(cards))
        player_hand.append(first_card)
        player_hand.append(second_card)
        bot_first_card = int(random.choice(cards))
        bot_hand.append(bot_first_card)

        player_score = calculat_score(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card:{bot_hand}")
        another_card = input("Type 'y' to get another card, type 'n' to pass:")
        if another_card == "n":
            bot_secord_card = int(random.choice(cards))
            bot_hand.append(bot_secord_card)
            check_ace(bot_hand)
            bot_score = calculat_score(bot_hand)
            print(f"Computer's second hand: {bot_secord_card}, final score: {bot_score}")
            if bot_score < 17:
                bot_third_card = int(random.choice(cards))
                bot_hand.append(bot_third_card)
                bot_score = calculat_score(bot_hand)
                print(f"Computer's third hand: {bot_third_card}, final score: {bot_score}")
                if bot_score < 17:
                    bot_third_card = int(random.choice(cards))
                    bot_hand.append(bot_third_card)
                    bot_score = calculat_score(bot_hand)
                    print(f"Computer's third hand: {bot_third_card}, final score: {bot_score}")
            if bot_score > 21:
                clear_screen()
                game_end = True
                print(blackjack_logo + "\n")
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Computer's final hand: {bot_hand}, final score: {bot_score}")
                print("Opponent went over. You win 😁")
            elif player_score == bot_score:
                clear_screen()
                game_end = True
                print(blackjack_logo + "\n")
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Computer's final hand: {bot_hand}, final score: {bot_score}")
                print("Draw 🙃")

            elif 21 <= player_score > bot_score:
                clear_screen()
                game_end = True
                print(blackjack_logo + "\n")
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Computer's final hand: {bot_hand}, final score: {bot_score}")
                print("You win 😃")

            elif player_score < bot_score <= 21:
                clear_screen()
                game_end = True
                print(blackjack_logo + "\n")
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Computer's final hand: {bot_hand}, final score: {bot_score}")
                print("You lose 😤")


        else:
            third_card = int(random.choice(cards))
            player_hand.append(third_card)
            check_ace(player_hand)
            player_score = calculat_score(player_hand)
            print(f"Computer's third hand: {player_hand}, final score: {player_score}")
            if player_score > 21:
                clear_screen()
                game_end = True
                print(blackjack_logo + "\n")
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print("You went over. You lose 😭")
    start()
def start():
    print(blackjack_logo + "\n")
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if game == "y":
        clear_screen()
        game_start = False
        print(blackjack_logo + "\n")
        blackjack(game_start)
    else:
        clear_screen()
        print("Have a good day!")


start()
