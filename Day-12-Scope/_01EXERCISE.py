
import random
print("Welcome to the Numbet Guessing Game1\v")
print("I am thinking of a number between 1 and 20\v")

level=input("choose a level 'easy' or 'hard'(e/h)\n")
if(level=="h"):
    chance=5
    
    number=random.randint(1,20)
    while chance>=1:
        guess=int(input("Enter your guess: "))
        if(guess>number):
            print("High")
        elif(guess==number):
            print("you win")
        else:
            print("low")
        chance=chance-1
        if(guess==number):
            print(f"Your won in  {5-chance} attempts")
        else:
            if(chance>=1):
                print(f"You have {chance} remaining")
            else:
                print("You lose")
            
    
elif(level=="e"):
    chance=10
    
    number=random.randint(1,100)
    while chance>=1:
        guess=int(input("Enter your guess: "))
        if(guess>number):
            print("High")
        elif(guess==number):
            print("you win")
        else:
            print("low")
        chance=chance-1
        if(guess==number):
            print(f"Your won in {10-chance} attempts")
        else:
            if(chance>=1):
                print(f"You have {chance} remaining")
            else:
                print("You lose")
else:
    print("wrong")

# by myself without any help
# keep it up boi sachin