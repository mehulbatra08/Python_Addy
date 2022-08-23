#Write a python program to read the text from a given file 'poem.txt' and find out whether it contains 
# the word 'twinkle'

# f = open("poem.txt", 'w')
# f.write("twinkle twinkle little star how i wonder what you are!")
# f.close()

f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
    f.close()