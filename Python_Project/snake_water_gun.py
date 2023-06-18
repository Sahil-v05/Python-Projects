import random

def gameWin(comp,you):
    if comp == you:
        return None 
    elif comp == 's':
        if you == 'w':
            return 'lose' 
        elif you == 'g':
            return 'win'
    elif comp == 'w':
        if you == 's':
            return 'win' 
        elif you == 'g':
            return 'lose'
    elif comp == 'g':
        if you == 's':
            return 'lose' 
        elif you == 'w':
            return 'win'

print("Comp Turn : Snake(s) Water(w) or Gun(g)")
randNo = random.randint(1,3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g' 
you = input("Player's Turn : Snake(s) Water(w) or Gun(g)")
a = gameWin(comp,you)
print(f'Computer chose {comp}')
print(f'you chose {you}')
if a == None:
    print('This game is tie')
elif a :
    print('You win!')
else:
    print ('You lose!')