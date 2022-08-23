# Write a Python program to guess a number between 1 to 9.

# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random
user_input = 0 
Computer_generated_number = random.randint(0,9)
while Computer_generated_number != user_input:
    user_input = int(input("Guess the number b/w 1 and 9\n"))


print("Well Guessed!")




    
