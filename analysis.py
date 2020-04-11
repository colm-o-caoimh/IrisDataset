# Colm O Caoimh
# PandS project 2020

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read file using genfromtxt
iris_data = np.genfromtxt("iris.data", delimiter=',')

# Code from Wikipedia 'Five Number Summary' page
def fivenum(data):
    return np.percentile(data, [0, 25, 50, 75, 100], interpolation='midpoint')

# Create dictionary of variable data for use in for loop
measurement_dict = {
    "sepal_length": iris_data[:,0],
    "sepal_width": iris_data[:,1],
    "petal_length": iris_data[:,2],
    "petal_width": iris_data[:,3],
}


# for loop outputs summary of data 
for measurement in measurement_dict:
    print(fivenum(measurement_dict[measurement]))
    

    