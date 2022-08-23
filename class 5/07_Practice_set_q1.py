#Write a prog. to create a dictionary of hindi words with values as their english translation.
#Provide user with an option to look up
myDict = {"khaana" : "food",
           "rasoda" : "kitchen"}

print("options are ", myDict.keys())
a  = input("Enter the hindi word\n")
print("The meaning of your word is:", myDict[a])

#Below line will not throw an error if the key is not present in the dictionary
#print("The meaning of your word is:", myDict.get(a))