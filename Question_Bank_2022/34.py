# . Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# my_string = ""
# for i in range(1,6):
#     my_string = "*" + my_string
#     print(my_string)


# u_string = ""
# for j in range(1,5):
#     u_string = "*" + u_string
#     print(u_string)

n=5;
for i in range(n):
    for j in range(i):
        print ('* ')
    print('')



  
    
