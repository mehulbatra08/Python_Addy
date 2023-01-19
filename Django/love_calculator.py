f_name = input("Enter the name one\n").lower()
l_name = input("Enter the name two\n").lower()
namesum = f_name + l_name
#Now I want to check true love in this string called namesum

t = namesum.count('t')
r = namesum.count('r')
u = namesum.count('u')
e = namesum.count('e')

first_person = t + r + u + e



l = namesum.count('l')
o = namesum.count('o')
v = namesum.count('v')
e_2 = namesum.count('e')

last_person = l + o + v + e_2


final_name = str(first_person) + str(last_person)

print(final_name)

