# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5.

pehla = int(input("Write the first integer, "  ))
dusra = int(input("write the dusra interger, "  ))

if pehla + dusra == 5 or pehla - dusra == 5 or pehla == dusra:
    print("True")

else:
    print("False")
    

