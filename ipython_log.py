# IPython log file

get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('run', 'ipython_log.py')
iris_data
get_ipython().run_line_magic('run', 'ipython_log.py.002~')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
iris_data = pd.read_csv('iris.data', header=None)
iris_data.shape
iris_data.head
iris_data.info()
quit()
