height=float(input("Enter your height in meter\n"));
weight=int(input("Enter your weight in kilo\n"))
bmi=weight/(height*height)
 
if bmi>35:
    print("Clinically obese")
elif(bmi>30 and bmi<35):
    print("obese")
elif(bmi>25 and bmi<30):
    print("overweight")
elif(bmi>18.5 and bmi<25):
    print("normal weight")
else:
    print("underweight")