#Write a program to find wether a given number is prime or not.


num = int(input("Enter the number: "))
prime = False
for i in range(2, num):
    if(num%i == 0):
        print("This number is prime")
        prime = True
        break
if prime:
    print("The number is not Prime")
else:
    print("Number is Prime")