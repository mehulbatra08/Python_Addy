#Write a python program to remove a green word from a string and strip it in at the same time.


#what is strip?

# this = "    Harry is good boy    "
# print(this)
# print(this.strip())     spaces ko add krde yeh strip wala function saath mein



def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.split()

this = "     Harry is a good boy   "
remove_and_split(this, "Harry")
# print(this)
# print(this.strip())

