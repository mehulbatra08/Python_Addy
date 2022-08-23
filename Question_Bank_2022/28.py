# Write a Python program to guess a number between 1 to 9

import random

a = int(input("Enter the number\n"))

b = random.randint(1,10)

while a  != b:
    b = int(input("Guess a number b/w 1 and 10"))
print("Well Guessed")