
import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == "Sc":
        if you == "P":
            return False
        elif you == "S":
            return True

    elif comp == "S":
        if you == "Sc":
            return False
        elif you == "P":
            return True

    elif comp == "P":
        if you == "S":
            return False
        elif you == "Sc":
            return True
print("Computer Turn: Stone(S), Paper(P) or Scissors(Sc) ?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'Sc'
elif randNo == 3:
    comp = 'P'

you = input("Your Turn: Stone(S), Paper(P) or Scissors(Sc) ?\n")

a = game(comp,you)

print(f"Computer choose : {comp}")
print(f"You choose : {you}")

if a == None:
    print("The game is Tie!")
elif a:
    print("You Win!")
    
else:
    print("You loose!")
    
   

