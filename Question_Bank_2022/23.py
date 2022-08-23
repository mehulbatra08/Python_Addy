# Write a Python program to get the n copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2.



n = int(input("Enter the value of n\n"))

x = str(input("Enter the value of the string\n"))

y = (x[0:2])

if len(x) >= 2:

    print(y*n)
else:
    print(x*n)
    