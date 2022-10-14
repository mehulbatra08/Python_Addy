# Write a Pandas program to convert the first column of a DataFrame as a Series

import pandas as pd

d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}

d1 = pd.Series(d['col1'])

print(d1)