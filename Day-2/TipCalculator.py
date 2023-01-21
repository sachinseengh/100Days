print("Welcome to tip Calculator\n")
Bill=float(input("What was the bill?$"))

Tip_percentage=int(input("what percentage tip would you like to give?10,12,15?\n"))

Tip_amount=Bill*(Tip_percentage/100)
Totalbill=Bill+Tip_amount
Number=int(input("In how many people you want to split the bill\n"))
print(f"Each people should pay {Totalbill/Number}")