#write a python function to print the first n lines of the following pattern

# * * *
# * *
# *                For n = 3

n = 3
for i in range(n):
    print("*" * (n-i)) #print * n-i times