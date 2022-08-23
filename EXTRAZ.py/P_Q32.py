# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

pehla = int(input("Enter pehla number, "  ))
dusra = int(input("Enter dusra number, "  ))
teesra = int(input("Enter teesra number "  ))

x = pehla + dusra + teesra

if pehla ==dusra or dusra == teesra or pehla == teesra:
    print("Sum is zero")

else:
    print(x)

    


