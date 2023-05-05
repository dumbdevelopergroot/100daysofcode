import random
#to print random integer between 1 and 10
random_int = random.randint(1,10)
print(random_int)
#to print random float between o and 1
random_float = random.random()
print(random_float)
#so now to print random float between 0 and 5, we just need to multiply with 5
random_float5 = random.random()*5
print(random_float5)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", 
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", 
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", 
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print((states_of_america)[0])


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", 
               "Pears", "Tomatoes", "Celery", "Potatoes"]