# local scope 
# the variable inside function and can only  be used inside that function


def name():
    name="sachin"
    print(name)

print(name())
# print(name) #it is not accessible


# Global variable can be used all around or inside the function

name="sachin"


def nameing():
    print(name)
nameing()