# -*- coding: utf-8 -*-
"""kaggle exercise

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vea5kVSCUWYwCJVd6rJgo5fkGaEKF__C
"""

import pandas as pd 
import numpy as np

# 1. How to create a series from a list, numpy array and dict?

import numpy as np
a_list = list("abcdefg")
numpy_array = np.arange(1, 10)
dictionary = {"A":  0, "B":1, "C":2, "D":3, "E":5}

series1 = pd.Series(a_list)
print(series1)
series2 = pd.Series(numpy_array)
print(series2)
series3 = pd.Series(dictionary)
print(series3)

# 2. How to combine many series to form a dataframe?
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

ser_df = pd.DataFrame(ser1, ser2).reset_index()
ser_df.head()
ser_df = pd.DataFrame({"col1":ser1, "col2":ser2})
ser_df.head(5)
ser_df = pd.concat([ser1, ser2], axis = 1)
ser_df.head()

# 3. How to get the items of series A not present in series B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser1[~ser1.isin(ser2)]

# 4. How to get the items not common to both series A and series B?
a_not_b = ser1[~ser1.isin(ser2)]
b_not_a = ser2[~ser2.isin(ser1)]
                          
a_not_b.append(b_not_a, ignore_index = True)

ser_u = pd.Series(np.union1d(ser1, ser2))
ser_i = pd.Series(np.intersect1d(ser1, ser2))
ser_u[~ser_u.isin(ser_i)]

# 5. How to get useful infos
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))
ser.describe()

# 6. How to get frequency counts of unique items of a series?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts()

# 7. How to convert a numpy array to a dataframe of given shape? (L1)
ser = pd.Series(np.random.randint(1, 10, 35))
ser

# pd.DataFrame(np.array(ser).reshape(7, 5))
pd.DataFrame(ser.values.reshape(7, 5))

# 8. How to find the positions of numbers that are multiples of 3 from a series?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, 10))
ser

# 9. How to extract items at given positions from a series?

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
ser.loc[pos]
ser.take(pos)

# 10. How to stack two series vertically and horizontally ?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
ser1.append(ser2)
pd.concat([ser1, ser2], axis = 0)
pd.concat([ser1, ser2], axis = 1)

# 11. How to get the positions of items of series A in another series B?
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

list(ser1[ser1.isin(ser2)].index)

[np.where(i == ser1)[0].tolist()[0] for i in ser2]
[pd.Index(ser1).get_loc(i) for i in ser2]

# 12. How to compute difference of differences between consequtive numbers of a series?
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
ser

ser.diff(periods = 1).tolist()
ser.diff(periods = 1).diff(periods = 1).tolist()

# 13. How to convert a series of date-strings to a timeseries?
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
ser

pd.to_datetime(ser)
from dateutil.parser import parse
ser.map(lambda x: parse(x))

# 14. How to filter words that contain atleast 2 vowels from a series?
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
ser

# 15. How to replace missing spaces in a string with the least frequent character?

# 16. How to change column values when importing csv to a dataframe?
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))