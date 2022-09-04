# Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

num_list = []
n = int(input(("Enter the value of n")))
for i in range(1,n+1):
    num_list.append(i)
# print(num_list)
even_list = []
odd_list = []
for num in num_list:
    if num%2 == 0:
        even_list.append(num)
        final_even = len(even_list)
    else:
        odd_list.append(num)
        final_odd = len(odd_list)
print(final_even)
print(final_odd)
