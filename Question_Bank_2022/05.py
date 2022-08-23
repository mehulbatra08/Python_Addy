# Write a Python program to accept a filename from the user and print the extension of that.


ram = (str(input("Enter the file name\n")))
final = ram.split(".")
print(final[1])