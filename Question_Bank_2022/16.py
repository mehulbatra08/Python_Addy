# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]


x = [12, 35 , 9 , 56 , 24]

x[0] = x[-1]

x[-1] = x[0]

print(x)