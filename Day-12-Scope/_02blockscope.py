# There is no block scope in python

# the variable declared inside the if else block can be accessed outside the if else block

game_level=5
enemies=["sachin","kumar","singh"]
if game_level>2:
    new_enemy=enemies[0]

print(new_enemy)
# if it is in function then we cant access it