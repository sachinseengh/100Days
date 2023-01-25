import random
name_string=input("Enter the elements of list seperated by comma\n")


name=name_string.split(",")  
# name1=len(name[0])
# print(name1)
print(f"{name[random.randint(0,(len(name)-1))]} is going to buy the meal today!")
