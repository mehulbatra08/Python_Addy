my_list = []
num = int(input("Enter the decimal number\n"))
while not num == 0:
    remainder = num%2
    my_list.append(remainder)
    num = num//2

# my_list.reverse()
empty_string =""
for i in my_list:
    new_string = str(i)
    empty_string = new_string + empty_string

print(empty_string)


