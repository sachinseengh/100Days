# Black jack game


import random
cards=[1,2,3,4,5,6,7,8,9,10]

my_cards=[]
computer=[]

agree=input("Do you want to play cards 21 game(y/n)\n")
if(agree=="y"):
    cardgiven=random.choice(cards)
    my_cards.append(cardgiven)
    cardtocomputer=random.choice(cards)
    computer.append(cardtocomputer)
  
    extracard=input("Do you want extra card(y/n)\n")
    while extracard=="y":
        extracard=extracard
        print(f"your cards={computer}")
        print(f"Computer card = {my_cards}")
        my_cards.append(random.choice(cards))
        computer.append(random.choice(cards))
    
    print(f"your cards={computer}")
    print(f"Computer card = {my_cards}")
    computer_sum=0
    my_sum=0
    for n in computer:
        computer_sum=computer_sum+n
    for n in my_cards:
        my_sum=my_sum+n
    print(f"computer = {computer}")
    print(f"your card  = {my_cards}")
    if(computer_sum>my_sum):
        print("computer Wins")
    else:
        print("You win")
    
else:
    print("get lost")




# Hurray i have successfully created this game without any help 
# keep it up boi sachin