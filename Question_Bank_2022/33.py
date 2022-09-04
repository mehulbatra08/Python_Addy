# Write a Python program to guess a number between 1 to 9.
import random
should_continue = True
while should_continue:
    user_guessed = int(input("Enter the Guessed number\n"))
    computer_guessed = random.randint(1,10)
    print(computer_guessed)

    if user_guessed == computer_guessed:
        print("You are correct!\n")
        should_continue = False

    else:
        print("Galat\n")
            
        