''' modes of opening a file
 
      r = open for reading
      w = open for writing
      a = open for appending
      t = open for updating 
      'rb' will open for read in binary mode
      'rt' will open for read in text mode'''

#n order to write a file, we first open it in write or append mode after which we use the pythons 
# f.write method to write the file!


f = open('another.txt','w')
f.write("I am appending!")
f.close()

#now we need to add more content to it