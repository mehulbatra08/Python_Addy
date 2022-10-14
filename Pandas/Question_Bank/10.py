# Write a Pandas program to add some data to an existing Series

from hashlib import new
import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])

new_s = s.append(pd.Series(['500','php']))

print(new_s)