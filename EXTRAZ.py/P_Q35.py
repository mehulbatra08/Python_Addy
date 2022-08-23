# Write a Python program to add two objects if both objects are an integer type.
def if_int(a,b):
    if type(a) == int and type(b) == int:
        print(a + b)
    else:
        print("not integers")
if_int(1,2)

#if you do if_int('aloo',2) error wil; be shown