#Write a program which finds out whether a given name is present in a list or not

myList = ["addy","baddy","daddy","maddy"]

name = input("Enter the name of the person\n")

if name in myList:
    print("Your name is present in the list")
else:
    print("your name is not present in the list")
