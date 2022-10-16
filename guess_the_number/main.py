#no. between 0-10
import random
val=random.randint(1,10)

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