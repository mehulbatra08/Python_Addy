#Write a python program to import calendar of a given month and year

import calendar 
y = int(input("year", ))
m = int(input("month", ))
print(calendar.month(y,m))