#Write a program to accept marks of 6 studensts and display them un a sorted manner


m1 = int(input("Enter marks of student Number 1"))
m2 = int(input("Enter marks of student Number 2"))
m3 = int(input("Enter marks of student Number 3"))
m4 = int(input("Enter marks of student Number 4"))
m5 = int(input("Enter marks of student Number 5"))
m6 = int(input("Enter marks of student Number 6"))

myList = [m1,m2,m3,m4,m5,m6]
myList.sort()
print(myList)