# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
current_age = int(age)
max_age = 90
remaining_years = max_age-current_age
remaining_months = remaining_years*12
remaining_weeks = remaining_years*52
remaining_days = remaining_years*365

print(f"you have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")



