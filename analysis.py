# Colm O Caoimh
# PandS project 2020

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read file using genfromtxt
iris_data = np.genfromtxt("iris.data", delimiter=',')

# Function to calculate 5 number summary for dataset
def fivenum(data):
    summary_points = np.percentile(data, [0, 25, 50, 75, 100], interpolation='midpoint')
    return summary_points

# Assign variable to each 5 number summary
sep_length = fivenum(iris_data[:,0])
sep_width = fivenum(iris_data[:,1])
pet_length = fivenum(iris_data[:,2])
pet_width = fivenum(iris_data[:,3])

# Combine each array into one 2d array. 
# Transpose for improved visualisation
summary_arr = np.vstack((sep_length, sep_width, pet_length, pet_width))
summary_arr = summary_arr.T

print(iris_data)

# Assign lables for rows and columns of dataframe
row_names = ['min.', '1st quart.', 'mean', '3rd quart.', 'max.']
col_names = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']

# Create dataframe for more effective presentation
summary_df = pd.DataFrame(summary_arr, index=row_names, columns=col_names)
print(summary_df)