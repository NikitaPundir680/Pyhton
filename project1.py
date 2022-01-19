import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == 'S':

        if you == 'W':
            return False
        elif you == 'G':
            return True
    elif comp == 'W':
        
        if you == 'G':
            return False
        elif you == 'S':
            return True
    elif comp == 'G':
        
        if you == 'S':
            return False
        elif you == 'W':
            return True
print("Computer Turn : Snake(S), Water(W) or Gun(G) ?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'W'
elif randNo == 3:
    comp = 'G'

you = input("Your Turn : Snake(S), Water(W) or Gun(G) ?\n")

a = game(comp,you)
print(f"Computer choose {comp} ")
print(f"You choose {you} ")

if a == None:
    print("The game is tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
