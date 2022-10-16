import random

print("Tic Tac Toe ")

values=[[' ' for i in range(3)] for j in range(3)]
positions=[i for i in range(9)]

def print_struct(values):
    print("\n")
    for element in values:
        for i,el in enumerate(element): 
            if((i+1)%3==0):
                print('| ',end="")
                print(el,end="")
                print(' |',end="\n\n")
            else:
                print('| ',end="")
                print(el,end="")
                print(' |',end="")

def result(val):
    winner=None
    if winner==None:
        for i in range(3):
            if (set(values[i]))=={f'{val}'}:
                return val                
    
    if winner==None:                
        for i in range(3):
            set_items=set({})
            for j in range(3):
                set_items.add(values[j][i])
            
            if (set(set_items))=={f'{val}'}:
                return val
    
    if winner==None:                
        if (values[0][0]==values[1][1]==values[2][2]==val):
            return val
        elif (values[0][2]==values[1][1]==values[2][0]==val):
            return val
    
    if not(positions) and winner==None:
        return "Tie"

def input_user():
    if positions:
        user=int(input("Enter a position : ")) 

        while user-1 not in positions:
            if user not in range(1,10): 
                print("Input should be between 1-9")
            else:
                print("Position is already used")
            user=int(input("Enter a new position : "))     
        
        if user-1 in positions:
            values[(user-1)//3][(user-1)%3]='x'
            print_struct(values)
            positions.remove(user-1)
            res=result('x')
            if res:
                if res=='x':
                    print("Yay! you win")
                    positions.clear()
                else:
                    print(res)
            else:
                input_comp()
    
def input_comp():
    if positions:
        comp=random.choice(positions)
        values[(comp)//3][(comp)%3]='o'
        print_struct(values)
        positions.remove(comp)
        res=result('o')
        if res:
            if res=='o':
                print("Computer wins!!")
                positions.clear()
            else:
                print(res)        

print_struct(values)

while positions:
    input_user()