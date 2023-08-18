#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')


display = []
for letter in chosen_word:
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()
    position = 0
    for letter in chosen_word:
        if letter == guess:
            display[position] = guess
        position += 1
    print(display)

print("You Win!")



