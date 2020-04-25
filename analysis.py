# Colm O Caoimh
# PandS project 2020

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Import data as pandas dataframe
iris_data = pd.read_csv('iris.data', header=None)

iris_data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

sns.set_style("darkgrid")
sns.lmplot(x='sepal_length', y='sepal_width', data=iris_data, fit_reg=False, hue='species')
plt.show()


'''
# Isolate columns according to data type
float_values = iris_data.iloc[:,0:4]
str_values = iris_data.iloc[:,4]

# Isolate each column for data manipulation
sep_len = iris_data.iloc[:,0]
sep_width = iris_data.iloc[:,1]
pet_len = iris_data.iloc[:,2]
pet_width = iris_data.iloc[:,3]
species = iris_data.iloc[:,4]


sns.pairplot(iris_data, kind="scatter", hue=species)

#sns.pairplot(diris_data, kind='scatter')
plt.show()
'''


'''
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=2, ncols=2)
ax1.scatter(sep_len, sep_width)
ax2.scatter(sep_len, pet_len)
ax3.scatter(sep_len, pet_width)
ax4.scatter(sep_width, pet_len)
#ax5.scatter(pet_len, pet_width)
#ax6.scatter(sep_width, pet_width)


plt.show()
'''


'''
# Write function which outputs scatterplot with each species coloured individually
# Code found on stackoverflow.com (see references)
def irisScatter(data1, data2, species):
    #fig, ax = plt.subplots()
    fig = plt.figure()
    fig.add_subplot()
    categories = np.unique(species)
    colors = np.linspace(0, 1, len(categories))
    colordict = dict(zip(categories, colors))
    species = species.apply(lambda x: colordict[x])
    plt.scatter(data1, data2, c=species)
    #ax.scatter(data1, data2, c=species)
    #fig.add_axes(ax)
    plt.show()
    return fig

irisScatter(sep_len, sep_width, species)
irisScatter(sep_len, pet_len, species)
#irisScatter(sep_len, pet_width, species)
#irisScatter(sep_width, pet_len, species)
#irisScatter(sep_width, pet_width, species)
#irisScatter(pet_len, pet_width, species)

#plt.show()
'''


'''
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
'''