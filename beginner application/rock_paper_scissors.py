import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
pick = [rock,paper,scissors]
print(pick[human_choice]+"\n")

bot_choice = random.randint(0,2)
print("Computer chose:")
print(pick[bot_choice]+"\n")

if human_choice == bot_choice:
    print("It's a draw")
elif human_choice == 0 and bot_choice == 2 or human_choice == 1 and bot_choice == 0 or human_choice == 2 and bot_choice == 1:
    print("You win!")
else:
    print("You lose")