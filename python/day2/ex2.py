#BMI calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
fheight = float(height)
fweight = float(weight)
BMI = (fweight/(fheight**2))
print(int(BMI))
#f-string example
print(f"Your BMI is {round(BMI,3)}") #here {} executes python code even inside double or single quotes