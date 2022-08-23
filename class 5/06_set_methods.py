# Creating an empty set
b = set()
print(type(b))

#Adding values to an empty set
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set

print(b)

#Lets observe weather we can add list in this set or not

b.add([4,5,6])

print(b) 
#We will get unhashable type list which means we cannot add list in set(same for dicitionary)

#but but but we can add tuple in this just use b.add((4,5,6))

# b.remove(5)  it will remove 5 from b
# b.remove(15) it will show error as there is no '15'
 