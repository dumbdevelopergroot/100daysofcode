#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
random_int = random.randint(1,10)
if random_int%2 == 0:
    print("Heads")
else:
    print("Tails")