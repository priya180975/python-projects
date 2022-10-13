#tic tac toe display 
#user 
#computer 

import random
from turtle import pos


print("Tic Tac Toe ")

# values=[' ' for i in range(9)]
positions=[i for i in range(9)]

#0-2
#3-5
#6-8

def print_struct(values):
    print("\n")

    for i,element in enumerate(values):
        if((i+1)%3==0):
            print('| ',end="")
            print(element,end="")
            print(' |',end="\n\n")
        else:
            print('| ',end="")
            print(element,end="")
            print(' |',end="")

def input_user():
    if positions:
        user=int(input("Enter a position : ")) 

        while user not in positions:
            if user not in range(9): 
                print("Input should be between 0-8")
            else:
                print("Position is already used")
            user=int(input("Enter a new position : "))     
        
        if user in positions:
            positions.remove(user)
            values[user]='x'
            print_struct(values)

        print(positions)
    else:
        result()

    
def input_comp():
    if positions:
        comp=random.choice(positions)
        positions.remove(comp)
        values[comp]='o'
        print_struct(values)

        print(positions)
    else:
        result()


def result():
    if not(positions):
        print("Exitt")


# print_struct(values)
# while positions:    
#     input_user()
#     input_comp()


# values=['x','x','o','x','x','x','x','x','x']
# res=[]
# check="x"

# if ((values[0]==values[1]==values[2]==check) or 
# (values[3]==values[4]==values[5]==check) or 
# (values[6]==values[7]==values[8]==check)):
#    print(check)

# elif ((values[0]==values[3]==values[6]==check) or 
# (values[1]==values[4]==values[7]==check) or 
# (values[2]==values[5]==values[8]==check)):
#    print(check)

# elif ((values[0]==values[4]==values[8]==check) or 
# (values[2]==values[4]==values[6]==check)):
#    print(check)
    