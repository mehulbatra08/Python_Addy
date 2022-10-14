# Write a Pandas program to convert a dictionary to a Pandas series

import pandas as pd

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

print(pd.Series(my_dict))
