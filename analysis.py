# Colm O Caoimh
# PandS project 2020

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read file using genfromtxt
iris_data = np.genfromtxt("iris.data", delimiter=',')


# Code from Wikipedia 'Five Number Summary' page
def fivenum(data):
    x = np.percentile(data, [0, 25, 50, 75, 100], interpolation='midpoint')
    return x


sepal_length = fivenum(iris_data[:,0])
sepal_width = fivenum(iris_data[:,1])
petal_length = fivenum(iris_data[:,2])
petal_width = fivenum(iris_data[:,3])

print(petal_length) 

'''
# Create dictionary of variable data for use in for loop
measurement_dict = {
    "sepal_length": iris_data[:,0],
    "sepal_width": iris_data[:,1],
    "petal_length": iris_data[:,2],
    "petal_width": iris_data[:,3],
}


# for loop outputs summary of data 
for measurement in measurement_dict:
    x = fivenum(measurement_dict[measurement])

print(x)
print(type(x))
 '''   

    