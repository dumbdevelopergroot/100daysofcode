height=int(input("Please enter your height in cm: "))
cost=0
if height<120:
    print("You cant ride")
else:
    age=int(input("Please enter your age: "))
    if age<=12:
        cost=5
        print("You will be charged $5")
    elif 12<age<18:
        cost=7
        print("You will be charged $7")
    elif 45<=age<=55:
        cost=0
    else:
        cost=12
        print("You will be charged $12")
    
    wants_photo=input("Do you want your photo taken? Y or N: ")
    if(wants_photo=="Y" or wants_photo=="y"):
        cost+=3
    print(f"Your final bill is ${cost}")