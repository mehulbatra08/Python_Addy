# Write a Pandas program to compare the elements of the two Pandas Series.

import pandas as pd

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])

print(ds1 == ds2)
print("Greater Than ")
print(ds1 > ds2)

print("Smaller than ")
print(ds1<ds2)

