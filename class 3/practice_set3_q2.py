#Write a program to fill in a letter template given below with name and date 
#                                         letter = ''' dear </name/>
#                                            You are selected
#                                            </Date/> '''


letter = '''Dear <|Name|>,
Date: <|DATE|>
congratulations. YOu are selected!
 '''
name = input("Enter your Name\n")
date = input("Enter your Date\n")
letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|DATE|>" , date)    
print(letter)                                                                   
                                                                    
