height=int(input("Please enter your height in cm: "))
if height<120:
    print("You cant ride")
else:
    age=int(input("\nPlease enter your age: "))
    if age<=12:
        print("You will be charged $5")
    elif 12<age<18:
        print("You will be charged $7")
    else:
        print("You will be charged $12")
