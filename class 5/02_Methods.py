myDict = { "fast": "In a Quicker manner",
"harry": "A coder",
"marks": [12,2,3],
"anotherdict": {'harry':'player'},
1:2
}

#Dictionary methods
print(list(myDict.keys())) #Print the keys of the dictionary
print(myDict.keys()) #Print the keys of the dictionary
print(myDict.items()) #print the keys (keys,value) for all contents on the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friend"
}
myDict.update(updateDict) #updates the dictionary by adding key value pairs from from updateDict
print(myDict)

print(myDict.get("Lovish")) #prints value associated with key "harry"
print(myDict["Lovish"]) #prints value associated with key "harry"


#the difference between .get and [] syntax in Dictionaries
print(myDict.get("Lovish2")) #returns none as harry2 is not present in dictionary
print(myDict["Lovish2"]) #throws an error as Lovish2 is not present in the dictionary