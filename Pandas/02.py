import pandas as pd
import numpy as np

ser = pd.Series(np.random.rand(34))
# print(ser) #Give random values from 0 to 34
# type(ser) #Give information about the ser

newdf = pd.DataFrame(np.random.rand(334,5),index = np.arange(334))
# print(newdf)

newdf.dtypes
newdf[0][0] = "Harry" #This will add a new string called harry at 0*0 position

# print(newdf)


# print(newdf.index)
print(newdf.columns)

# print(newdf.T) Transpose the matrix i.e change the rows and coloumn
newdf.sort_index(axis=0, ascending=False )

