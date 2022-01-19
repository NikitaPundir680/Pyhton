import random

def game(comp,you): #function game
    if comp == you: #if both comp and you has choose same 
        return None
    elif comp == 'S':

        if you == 'W':
            return False #you will loose
        elif you == 'G':
            return True #you will win 
    elif comp == 'W':
        
        if you == 'G':
            return False #you will loose
        elif you == 'S':
            return True #you will win 
    elif comp == 'G':
        
        if you == 'S':
            return False #you will loose
        elif you == 'W':
            return True #you will win 
print("Computer Turn : Snake(S), Water(W) or Gun(G) ?")
randNo = random.randint(1,3)#for randome number generation b/w 1 and 3
if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'W'
elif randNo == 3:
    comp = 'G'

you = input("Your Turn : Snake(S), Water(W) or Gun(G) ?\n")

a = game(comp,you)#function call
print(f"Computer choose {comp} ")
print(f"You choose {you} ")

if a == None:
    print("The game is tie!") #if both comp and you has choosen same then print tie
elif a:
    print("You Win!")
else:
    print("You Lose!")
