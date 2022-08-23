# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.





x = str(input("Enter the sentence\n"))

y = x.split(" ")

print(y)

if (y[0]) == "Is":
    print(x)

else:
    print("Is",x)