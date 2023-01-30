# putting a dictionary as a value 

my_dict={
    'visited':['s','b','v'],
    2:"hllo"
}
print(my_dict["visited"][0])

# Note we can nest a list inside another list 

# Nesting dictionary in another dictionary


dict={
    "visited":{
        "citi_visited":["paris","moscow","burma"]
    },
    "not_visited":"Delhi"
}
print(dict["visited"])


# we can also nest dict into list


list=[
    {
        "name":"sachin"
    },
    {
        "address":"Bharatpur"
    }
]
print(list)