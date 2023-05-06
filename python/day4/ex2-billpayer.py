# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#method 1
random_number = random.randint(0,len(names)-1)
bill_payer = names[random_number]
#metod 2
# use random.choice() method
bill_payer=random.choice(names)
print(f"{bill_payer} is going to buy the meal today!")