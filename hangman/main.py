from random_word import RandomWords #pip install random_word
r = RandomWords()
word=r.get_random_word()
loading="...loading word"
while type(word)!=str or word.isalpha()==False:
    print(loading)
    word=r.get_random_word()
word=word.lower()

print("\n")

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

word_letters=[i for i in word]
display_word=['-' for _ in word]
used_letters=[]

def display_status():
    for i in display_word:
        print(i.upper(),end="")
    print()
    print("used letters : ", used_letters) 

def guess_display(guess):
    for i,element in enumerate(word_letters):
        if(element==guess):
            display_word[i]=guess

def guess_alphabets():
    lives=6
    while lives>0:
        guess=input("Enter a letter : ")
        
        if guess not in alphabets:
            print("not a valid letter")
        elif guess in used_letters:
            print("letter already used")
        else:
            used_letters.append(guess)
            if guess in word_letters:
                guess_display(guess)
            else:
                lives-=1
            display_status()
            print("lives remaining : ",lives)
            if display_word==word_letters:
                print(f"\n Yay! you have guessed the word {word}")
                break
        print()
    else:
        print(f"\n You failed! the word was {word}")

    



display_status() 
guess_alphabets()
