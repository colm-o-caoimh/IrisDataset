import numpy as np
import matplotlib.pyplot as plt

iris_data = np.genfromtxt("iris.data", delimiter=',')

#print(iris_data[:,0])

sepal_length = iris_data[:,0]

# mean (rounded to 3 decimal places)
mean = round(np.mean(sepal_length), 3)
print("Sepal length mean: ", mean)

# max lingth
max_length = max(sepal_length)
print("Sepal length max: ", max_length)

# min length
min_length = min(sepal_length)
print("Sepal length min: ", min_length)

# 1st quartile
first_quartile = np.percentile(sepal_length, 25)
print(first_quartile)

# 3rd quartile
third_quartile = np.percentile(sepal_length, 75)
print(third_quartile)

# median
median = np.median(sepal_length)
print(median)