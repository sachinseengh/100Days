# While wrinting the key,the key must be a string or a number .

dict={"1":"sachin","2":"dipesh","bug":"surya"}

# Retriving the items
print(dict["bug"])

# Adding new items to dictionary
dict["debug"]="hello this is me debugger"

print(dict)

# creating empty dictionary
empty_dictionary={ }

# clearing all the items of dictionary
# dict={ }
# print(dict)    #{ }

# edit the value 
dict["bug"]="sachin"
print(dict)


# Looping over dictionary
for thing in dict:
    print(thing)
    print(dict[thing])