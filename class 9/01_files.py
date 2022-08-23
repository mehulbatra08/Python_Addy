#first make a txt file by typing 
# f = open("mehul.txt","w") #now mehul.txt file will be made and w means write 
#now in the next commands r is written which means read and it will read from mehul.txt







f = open("mehul.txt", "r")
content = f.read()

print(content)
f.close()