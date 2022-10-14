import csv
import numpy as np
import pandas as pd
my_dict = {
    "Name" :["Addy","Rohan","Munna","lalu"],
    "Marks": [24,45,48,21],
    "City":["Mumbai","Lucknow","Pune","Sadak"] 
}

final = pd.DataFrame(my_dict)

# print(final)

# final.to_csv("friends.csv")#This will Export as CSV

# final.to_csv("friends_index_False.csv",index = False)
print(final.describe()) #Describe function will give you the mean,Frequency,Maximum number etc from the data

# harry = pd.read_csv("") This will read the value of the particular Csv File





