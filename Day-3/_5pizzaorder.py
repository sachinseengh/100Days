print("Welcome to pizza order bot\n")
size=input("Enter the size of pizza u want (L,M,S)\n");
pepperoni=input("Do you want pepporoni (Y/N)\n")
extra_cheese=input("Do you want extra cheese(Y/N)\n")

if(size=="S"):
    if(pepperoni=="Y"):
        if(extra_cheese=="Y"):
            print(f"Your bill is ${15+2+1}")
        else:
            print(f"Your bill is {15+2}")
    else:
        print(f"Your bill is $15")
elif(size=="M"):
     if(pepperoni=="Y"):
        if(extra_cheese=="Y"):
            print(f"Your bill is ${20+3+1}")
        else:
            print(f"Your bill is ${15+3}")
     else:
        print(f"Your bill is $20")
elif(size=="L"):
     if(pepperoni=="Y"):
        if(extra_cheese=="Y"):
            print(f"Your bill is ${25+3+1}")
        else:
            print(f"Your bill is ${25+3}")
     else:
        print(f"Your bill is $25")
else:
    print("Wrong input enter only the Upper case character")
