height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight/(height**2))
status = ""
if BMI>=35:
    status="are clinically obese"
elif 30<BMI<=35:
    status="are obese"
elif 25<BMI<=30:
    status="are slightly overweight"
elif 18.5<=25:
    status="have a normal weight"
else:
    status = "are underweight"

print(f"your BMI is {BMI}, you {status}")