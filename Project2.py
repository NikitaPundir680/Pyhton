
import random

def game(comp,you): #function game
    if comp == you:#if both comp and you has choose same 
        return None
    elif comp == "Sc":
        if you == "P":
            return False#you will loose
        elif you == "S":
            return True#you will win 

    elif comp == "S":
        if you == "Sc":
            return False#you will loose
        elif you == "P":
            return True#you will win 

    elif comp == "P":
        if you == "S":
            return False#you will loose
        elif you == "Sc":
            return True#you will win 
print("Computer Turn: Stone(S), Paper(P) or Scissors(Sc) ?")
randNo = random.randint(1,3)#for randome number generation b/w 1 and 3
if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'Sc'
elif randNo == 3:
    comp = 'P'

you = input("Your Turn: Stone(S), Paper(P) or Scissors(Sc) ?\n")

a = game(comp,you)#function call

print(f"Computer choose : {comp}")
print(f"You choose : {you}")

if a == None:
    print("The game is Tie!")#if both comp and you has choosen same then print tie
elif a:
    print("You Win!")
    
else:
    print("You loose!")
    
   

