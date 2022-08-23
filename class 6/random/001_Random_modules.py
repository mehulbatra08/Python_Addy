import random
random_integer = random.randint(1,10)
print(random_integer)

# random_float = random.random()
# print(random_float)

#Now what if i need this random from 0.00000000 to 4.9999999?
#I will have to multiply the current scenario with 5

random_float = random.random()*5
print(random_float)
