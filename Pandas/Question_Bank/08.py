# Write a Pandas program to convert Series of lists to one Series

import pandas as pd

series_list = {0:['Red','Green','White'],1:['Red','Black'],2:['Black']}
combined_series = pd.Series(series_list[0]+series_list[1]+series_list[2])

print(combined_series)