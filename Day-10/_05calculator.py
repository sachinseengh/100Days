def sum(n,n2):
    return n+n2

def subtract(n,n2):
    return n-n2
def multiply(n,n2):
    return n*n2
def divide(n,n2):
    return n/n2

n=int(input("Enter your first number"))
n2=int(input("Enter your second number\n"))
print(f"sum is {sum(n,n2)}")
print(f"multiply is {multiply(n,n2)}")
print(f"divide is {divide(n,n2)}")
