# IPython log file

get_ipython().run_line_magic('logstart', '')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
iris_data = pd.read_csv('iris.data', header=None)
sep_len = iris_data.iloc[:,0]
sep_width = iris_data.iloc[:,1]
pet_len = iris_data.iloc[:,2]
pet_width = iris_data.iloc[:,3]
species = iris_data.iloc[:,4]
plt.scatter(sep_len, sep_width)
species.unique()
get_ipython().run_line_magic('matplotlib', 'inline')
species.unique()
uniq = species.unique()
len(uniq)
fig, ax = plt.subplots()
fig, ax = plt.subplots(nrows=5, ncols=5)
plt.show()
type(x)
type(ax)
fig, ax = plt.subplots()
type(ax)
fig, ax = plt.subplots(nrows=5, ncols=5)
ax
squares = [i * i for i in range(10)]
square
squares
plt.scatter(sep_len, sep_width)
plt.scatter(sep_len, sep_width)
plt.show()
quit()
