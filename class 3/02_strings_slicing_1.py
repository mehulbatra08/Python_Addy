greeting = "Good morning, "
name = "Mehul"

print(greeting + name)
#2 Method (concatinating two strings)
c = greeting + name
print(c)
                                       #In python we give number to the word
                                       # M=0 E=1 H=2 U= 3 L = 4
                                       # this is called slicing !
print(name[1])
print(name[4])    #We use square bracket for slicing 
                  # name[3] = "d"...> does not work(we cant change any value)
 #Now what actually is Slicing?

print(name[0:3])    #It will show 012 but 3 will be excluded (MEH)            
print(name[1:3])
print(name[:4])      #instead of zero we can put nothing result will be same as name[0:4]
print(name[1:])      #is same as name[1:4]



c = name[-4:-1] #is same as name[1:4]
print(c)


d = name[1:4:2]   #at end we have used 2 which means har dusre character ko print krdo
print(d)
#for further knowledge lets move to the next slide