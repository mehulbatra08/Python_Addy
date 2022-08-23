# Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.

pehla = int(input("Enter the number, "  ))
dusra = int(input("Enter the number, "  ))

x = pehla + dusra

if 15<=x<=20:
    print("20")

else:
    print(x)