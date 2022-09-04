# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

c = int(input("Enter the temperature in Celcius\n"))
f = print((c/5*9) + 32)


f = int(input("Enter the temperature in Farenhite\n"))

c = ((f-32))*5/9

print(c)