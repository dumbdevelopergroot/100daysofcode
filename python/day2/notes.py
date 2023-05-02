num = 5
print(type(num))
#type conversion
#num_char =
# len(input("enter a name: "))

# above line throws type error because len() gives integer output which we cant concatenate with 
# string type without conversion. so, 
num_char = str(len(input("enter a name: ")))
# above line converts len() output to a string.
print("your name has "+num_char+" characters")
