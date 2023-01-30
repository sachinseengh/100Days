
# i will check it later

def prime_checker(number):
    count=0
    if number<=1:
        print("Number less than or equal to 1")
    else:
        count=0
        for i in range(2,number):
            if(number%i == 0):
                count=1
    if(count==1):
        print("prime")
        

prime_checker(5)
