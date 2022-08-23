# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum


x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
z = int(input("Enter the value of z : "))


sum = (x+y+z)



if(x==y==z):
    print(sum*3)
else:
    print(sum)