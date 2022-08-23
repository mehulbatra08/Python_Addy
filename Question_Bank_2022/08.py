# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615



# x = 2
# y = 5
# z = int(str(x) + str(y))

# print(z)

# print(z + 25)



x = int(input("Enter the value of number\n"))

z = int(str(x) + str(x))

y = int(str(x)+ str(x) + str(x))


print(x+y+z)

