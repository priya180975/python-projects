#no. between 0-10
import random
val=random.randint(1,10)

print("----------------------\nuser guess")
def user_guess():
    guess=int(input("Guess a number between 1-10:"))
    while guess!=val:
        if guess<val:
            print(f"Value is greater than {guess}")
            guess=int(input("Guess a value :"))
        else:
            print(f"Value is less than {guess}")
            guess=int(input("Guess a value :"))
    print(f"Yay!! you have guessed the value {val}")

user_guess()


print("----------------------\ncomputer guess")
print("Think of a value between 0 and 100 ")

def computer_guess():
    c_guess=random.randint(0,100)
    judge=input(f"Is {c_guess} high(H), low(L) or correct (C) :")
    low=0
    high=100
    while judge.lower()!='c':

        if low==high:
            print(f"Your number must be {low}")
            break

        elif judge.lower()=='l':
            if c_guess>=high:
                print("Invalid")
            else:
                low=c_guess+1
                c_guess=random.randint(low,high)
            judge=input(f"Is {c_guess} high(H), low(L) or correct (C) :")
        
        elif judge.lower()=='h':
            if c_guess<=low:
                print("Invalid")
            else:
                high=c_guess-1
                c_guess=random.randint(low,high)
            judge=input(f"Is {c_guess} high(H), low(L) or correct (C) :")
        
        else:
            print("wrong input")
            judge=input(f"Is {c_guess} high(H), low(L) or correct (C) :")
    else:
        print(f"Yay!! computer guessed your number {c_guess}")

computer_guess()

