# function to add  add_new_country("Russia",2,["moscow","saint petersburg"])


travel_log=[ ]

def add_new_country(country,time,cities):
    new_country={}
    new_country['country']=country
    new_country['Visits']=time
    new_country['cities']=cities
    travel_log.append(new_country)
    
add_new_country("nepal",2,["moscow","saint petersburg"])
print(travel_log)