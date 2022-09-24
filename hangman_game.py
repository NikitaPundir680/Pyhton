import random
life_stages = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========
''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========
''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
========
''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
========
''','''
 +---+
 |   |
 O   |
     |
     |
     |
========
''','''
 +---+
 |   |
     |
     |
     |
     |
========
''']
from hangaman_list import logo
print(logo)
import hangaman_list
end_of_game=False

chosen_word = random.choice(hangaman_list.word_list)

#user's lives
lives = 6
#for creating blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    user = input("Guess a letter: ").lower()
    if user in display:
        print(f"You already guessed {user}.")
    #checking the guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user:
            display[position]=letter
    print(display)
    if user not in chosen_word:
        print(f"You gueesed a wrong letter i.e {user}.You loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!!")
    
    #joining the all letters in a string

    if "_" not in display:
        end_of_game=True
        print("You Win!!")
    print(life_stages[lives])