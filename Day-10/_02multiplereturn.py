def name(firstname,secondname):
    greet=f"Hello {firstname.title()} {secondname.title()}"
    return greet

print(name(input("Enter your first name\n"),input("Enter your second name\n")))