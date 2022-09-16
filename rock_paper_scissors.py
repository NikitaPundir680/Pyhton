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

#Write your code below this line 👇
game_images = [rock,paper,scissors]
user = int(input('Choose 0 for "rock", 1 for "paper" and 2 for "scissors":\n'))

computer = random.randint(0,2)


if user >= 3 or user<0:
  print("Invalid number,Please choose among 0,1,2!")
else:
  print("You choose!\n"+ game_images[user])
  print("Computer choose!\n"+ game_images[computer])

if user == computer:
  print("Match is draw!")
elif user == 0 and computer == 1:
  print("You loose!")
elif user == 1 and computer == 0:
  print("You win!")
elif user == 2 and computer == 1:
  print("You win!")
elif user == 2 and computer == 0:
  print("You loose!")
elif user == 0 and computer == 2:
  print("You win!")
elif user == 1 and computer == 2:
  print("You loose!")
  