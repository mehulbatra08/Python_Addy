#write a program to print multiplication table of a given number using a for loop.

num = int(input("Enter the number"))
for i in range(1,11):
    print(str(num)+ "x"+ str(i)+ "=" + str(i*num))

    #I can also use f function
# print(f"{num}X{i}={num*i}")