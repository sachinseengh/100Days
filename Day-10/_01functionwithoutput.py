# function that give us output

def my_function():
    result=3+2
    return result

print(my_function())

# .title() capitalize all the first letter of every word
def name(firstname,secondname):
    greet=f"Hello {firstname.title()} {secondname.title()}"
    return greet

print(name("sachin ","singh"))