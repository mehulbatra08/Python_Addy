# Write a Python program to accept a filename from the user and print the extension of that


name = input("enter the filename\n"  )
x = name.split(".")
#print(x) this will give us the whole name for eg hello.doc but we want only .doc

print(x[-1]) #therefore we use[-1]  

