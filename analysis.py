# Colm O Caoimh
# PandS project 2020

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Import data as pandas dataframe
iris_data = pd.read_csv('iris.data', header=None)

# View first 10 rows of dataset
#print(iris_data.head(10))

# assign column headers
iris_data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Isolate columns according to variable and data type
float_values = iris_data.iloc[:,0:4]
str_values = iris_data.iloc[:,4]



# A. Output a summary of each variable to a single txt file.



# Use describe() function to summarise data
float_summary = float_values.describe()
str_summary = str_values.describe()

# Establish 3 unique values in str_summary.
# This creates an array of each value.
str_summary = str_values.unique()

# Transpose str_summary array and convert to dataframe
str_summary = str_summary[:, None]
str_summary = pd.DataFrame({"Species": str_summary[:, 0]})

# Format string variable summary
# Add column containing quantity of unique values
quantity = ['50', '50', '50']
str_summary['Count'] = quantity

# Rename rows in str_summary
str_summary.index = ['Species_A', 'Species_B', 'Species_C']

# Format summary output and write to text file
with open("iris_summary.txt", "w") as f:
    heading = "SUMMARY OF VARIABLES IN IRIS DATASET" 
    f.write(heading + "\n")
    f.write("=" * len(heading) + "\n\n")
    f.write(float_summary.to_string() + "\n\n")
    f.write(str_summary.to_string())



# B. Save a histogram of each variable to png files


# Assign each column to a variable for easier manipulation
sep_len = iris_data['sepal_length']
sep_width = iris_data['sepal_width']
pet_len = iris_data['petal_length']
pet_width = iris_data['petal_width']
species = iris_data['species']


# Write a function which outputs a histogram for each dataset variable and saves
# it as a png file.
# First for numeric variables
def var_hist(var_data, fig_num, x_label, y_label, title, filepath):
    plt.figure(fig_num)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.hist(var_data, bins=20, rwidth=0.9,)
    plt.savefig(filepath)
    plt.close()

# Then for string variable 
def var_hist2(var_data, fig_num, x_label, y_label, title, filepath):
    plt.figure(fig_num)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.hist(var_data, bins=3, rwidth=0.9)
    plt.savefig(filepath)
    plt.close()

# Call function for each variable
var_hist(sep_len, 1, 'sepal_length_cm', 'count', 'Sepal Length', 'sepal_length.png')
var_hist(sep_width, 2, 'sepal_width_cm', 'count', 'Sepal Width', 'sepal_width.png')
var_hist(pet_len, 3, 'petal_length_cm', 'count', 'Petal Length', 'petal_length.png')
var_hist(pet_width, 4, 'petal_width_cm', 'count', 'Petal Width', 'petal_width.png')
var_hist2(species, 5, 'species', 'count', 'Iris Species', 'species.png')



# C. Output a scatter plot of each pair of variables



def scatter(x, y):
    sns.set(style="darkgrid")
    sns.lmplot(x, y, iris_data, fit_reg=False, hue='species')
    plt.show()

scatter('sepal_length', 'sepal_width',)
scatter('sepal_length', 'petal_length',)
scatter('sepal_length', 'petal_width',)
scatter('sepal_width', 'petal_length',)
scatter('sepal_width', 'petal_width',)
scatter('petal_length', 'petal_width')


# Create scatter plot with seaborn. colour by categorical variable
#sns.set(style="darkgrid")
#sns.lmplot(x='sepal_length', y='sepal_width', data=iris_data, fit_reg=False, hue='species')
#plt.show()

#sns.pairplot(iris_data, kind="scatter", hue='species')

#sns.pairplot(data=iris_data, kind='scatter')
#plt.show()