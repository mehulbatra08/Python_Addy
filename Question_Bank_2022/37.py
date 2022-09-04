# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5



my_list = []
for i in range(6):
    if i == 3 or i == 6:
        continue
    else:
        my_list.append(i)

print(my_list)

    