# Colm O Caoimh
# PandS project 2020

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import data as pandas dataframe
iris_data = pd.read_csv('iris.data', header=None)

# Isolate columns according to data type
float_values = iris_data.iloc[:,0:4]
str_values = iris_data.iloc[:,4]

# Use describe() function to summarise data
float_summary = round(float_values.describe(), 3)
str_summary = str_values.describe()

# Rename columns and rows in float_summary
float_summary.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
float_summary.rename(index={"25%": "1st quart.", "50%": "median", "75%": "3rd quart."}, inplace=True)

# Establish 3 unique values in str_summary
str_summary = str_values.unique()

# Transpose str_summary array and convert to dataframe
str_summary = str_summary[:, None]
str_summary = pd.DataFrame({"Species": str_summary[:, 0]})

# Add column containing quantity of unique values
quantity = ['50', '50', '50']
str_summary['Count'] = quantity

# Rename rows in str_summary
str_summary.index = ['Type_A', 'Type_B', 'Type_C']

# Write summary output to text file
with open("iris_summary.txt", "w") as f:
    f.write("SUMMARY OF VARIABLES IN IRIS DATASET\n\n")
    f.write(float_summary.to_string() + "\n\n")
    f.write(str_summary.to_string())