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
str_summary.index = ['Species_A', 'Species_B', 'Species_C']

# Write and format summary output to text file
with open("iris_summary.txt", "w") as f:
    heading = "SUMMARY OF VARIABLES IN IRIS DATASET" 
    f.write(heading + "\n")
    f.write("=" * len(heading) + "\n\n")
    f.write(float_summary.to_string() + "\n\n")
    f.write(str_summary.to_string())



# create variable for dataset variable
sep_len = iris_data.iloc[:,0]
sep_width = iris_data.iloc[:,1]
pet_len = iris_data.iloc[:,2]
pet_width = iris_data.iloc[:,3]
species = iris_data.iloc[:,4]

# write function which outputs a histogram for each dataset variable
def var_hist(var_data, fig_num, x_label, y_label, title, filepath):
    plt.figure(fig_num)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.hist(var_data, bins=20, rwidth=0.9,)
    plt.savefig(filepath)

def var_hist2(var_data, fig_num, x_label, y_label, title, filepath):
    plt.figure(fig_num)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.hist(var_data, bins=3, rwidth=0.9)
    plt.savefig(filepath)

var_hist(sep_len, 1, 'sepal_length_cm', 'count', 'Sepal Length', 'sepal_length.png')
var_hist(sep_width, 2, 'sepal_width_cm', 'count', 'Sepal Width', 'sepal_width.png')
var_hist(pet_len, 3, 'petal_length_cm', 'count', 'Petal Length', 'petal_length.png')
var_hist(pet_width, 4, 'petal_width_cm', 'count', 'Petal Width', 'petal_width.png')
var_hist2(species, 5, 'species', 'count', 'Iris Species', 'species.png')
