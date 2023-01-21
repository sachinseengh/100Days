name1=input("Enter your name\n")
name2=input("Enter your crush name\n")

together=(name1+name2).lower()

t=together.count('t')
r=together.count('r')
u=together.count('u')
e=together.count('e')

l=together.count('l')
o=together.count('o')
v=together.count('v')
e=together.count('e')

print(f"Your love percentage is {t+r+u+e}{l+o+v+e}%")