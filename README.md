# PAS2020_project
Final project Programming and Scripting 2020

## Introduction
* In this project I investigate the famous Iris data set using Python. The text editor I used is Visual 
Studio Code.

## Data search and download
* Following a simple Google search, one quickly establishes that the Iris data set is used widely
in the fields of machine learning and statistics. It is referenced in
numerous academic publications, student projects, online tutorials etc. and there
is no shortage of sources offering the file for download. The most commonly 
referenced source appears to be the UCI (University of California Irvine) [website](https://archive.ics.uci.edu/ml/datasets/Iris),
whose machine learning repository offers the data set for download.
It is this source that I have used in this project.

* It is important to mention that the UCI data set differs slightly from the data 
presented in Fisher's original paper. This is noted in the dataset documentation.

## Iris data set
* The data was collected by Edgar Anderson and introduced by Ronald A. Fisher in his
paper "The use of multiple measurements in taxonomic problems" in 1936. According
to the UCI website, the paper "... is a classic in the field [of pattern recognition]
and is referenced frequently to this day" [[1]](#1)

* A multivariate data set, it contains a total of 150 instances consisting of 50 instances
of each of 3 classes: *Iris-setosa*, *Iris-virginica* and *Iris-versicolor*. These refer
to 3 different species of the iris flower. There are 4 attributes in the sample: *sepal length*,
*sepal width*, *petal length* and *petal width*, referring to the parts of each flower
measured by Anderson.

## Python Libraries
**NumPy**: NumPy is roundly described as the fundamental package for scientific computing
and data analysis with Python [[2]](#2). Among the numerous other important features it contains,
NumPy's ndarray object allows for vectorized mathematical operations which is essential for 
any investigation and analysis of data.

**Pandas**: Pandas is built on the NumPy package and is a high-level data manipulation tool [[3]](#3).
The key data structure associated with Pandas is the DataFrame, which orders data in tables of
rows (observations) and columns (variables).

**Matplotlib.pyplot**: For data visualisation, Matplotlib is the fundamental library for the
Python programming language. It provides the underlying structure for many other visualisation libraries
in Python e.g. Seaborn, Holoviews. [[4]](#4) The pyplot module is used in this project for the generation
of histograms to investigate each variable in the data set.

**Seaborn**: Seaborn is built on Matplotlib and provides a "... high level interface for drawing
statistical graphics..." [[5]](#5) It uses much fewer lines of code for certain plot types, when compared
with Matplotlib, which can be quite verbose. In this project I have utlised Seaborn for the 
purpose of generating insightful scatter plots with minimal lines of code. 

## Importing the data
* Initial attempts to import the data involved using NumPy's `loadtxt()` and `genfromtxt()` functions.
However I eventually settled on Pandas:

`iris_data = pd.read_csv('iris.data', header=None)`

This loads the data as a DataFrame which enables easier manipulation throughout the program. In addition,
I found Pandas' handling of string objects to be more intuitive than NumPy's.


## Investigating the data
I found the quickest and most effective way to perform initial investigation on the data was to set 
up an interactive environment with ipython:

**Number of rows and columns:**

```python
In [10]: iris_data.shape
```
```
Out[10]: (150, 5)
```

**First five and last five rows:**

```python
In [11]: iris_data.head
```
```                                                 
Out[11]:                                                                
<bound method NDFrame.head of        0    1    2    3               4   
0    5.1  3.5  1.4  0.2     Iris-setosa                                 
1    4.9  3.0  1.4  0.2     Iris-setosa                                 
2    4.7  3.2  1.3  0.2     Iris-setosa                                 
3    4.6  3.1  1.5  0.2     Iris-setosa                                 
4    5.0  3.6  1.4  0.2     Iris-setosa                                 
..   ...  ...  ...  ...             ...                                 
145  6.7  3.0  5.2  2.3  Iris-virginica                                 
146  6.3  2.5  5.0  1.9  Iris-virginica                                 
147  6.5  3.0  5.2  2.0  Iris-virginica                                 
148  6.2  3.4  5.4  2.3  Iris-virginica                                 
149  5.9  3.0  5.1  1.8  Iris-virginica                                 
                                                                        
[150 rows x 5 columns]>
```                                                 

**Display data type of each column:**

```python
In [12]: iris_data.info()
```
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
0    150 non-null float64
1    150 non-null float64
2    150 non-null float64
3    150 non-null float64
4    150 non-null object
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
```

## Summary of each variable
* Following initial investigation above, we know that of the five variables in the data set,
4 contain float values. These represent the attributes of each of the 3 classes. The fifth
variable contains string values, displayed above as an `object`. 

* In order to provide a summary of each variable, I used the **Five-Number Summary** as a
basic framework. Mathematician John Tukey is credited with having first recommended its usage
in the analysis of a data set [[6]](#6). It involves calculating the minimum, 1st quartile, 
median, 3rd quartile and maximum of a data set in order to describe its distribution.

* I first grouped the variables according to data type:

```python
# Isolate columns according to data type
float_values = iris_data.iloc[:,0:4]
str_values = iris_data.iloc[:,4]
```

* For the numeric data, I initially calculated each statistic using the `max()`, `min()` and `median()` functions before 
applying NumPy's `percentile()` function to the data. I subsequently discovered Pandas `describe()`
method [[7]](#7) which outputs a DataFrame containing the relevant statistical information.

* For the dependent variable summary, I used `describe()` once more. A number of additional steps
were needed to output the information in the same tabular format as above. 
`str_summary.unique()` creates an `nparray` of each of target variable. This array was then 
converted to a DataFrame to get the desired format for output. Both tables were written to a txt file:

```python
# Use describe function to summarise data
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
    f.write("=" * len(heading) + "\n\n\n\n")
    heading2 = "NUMERIC VARIABLE SUMMARY"
    f.write(heading2 + "\n")
    f.write("=" * len(heading2) + "\n")
    f.write(float_summary.to_string() + "\n\n\n\n")
    heading3 = "DEPENDENT VARIABLE SUMMARY"
    f.write(heading3 + "\n")
    f.write("=" * len(heading3) + "\n")
    f.write(str_summary.to_string())
```

**Output (numeric variable summary):**

```
       sepal_length  sepal_width  petal_length  petal_width 
count    150.000000   150.000000    150.000000   150.000000 
mean       5.843333     3.054000      3.758667     1.198667 
std        0.828066     0.433594      1.764420     0.763161 
min        4.300000     2.000000      1.000000     0.100000 
25%        5.100000     2.800000      1.600000     0.300000 
50%        5.800000     3.000000      4.350000     1.300000 
75%        6.400000     3.300000      5.100000     1.800000 
max        7.900000     4.400000      6.900000     2.500000 
```

* From this table we can deduce that the sepal is larger in size than the petal on average.
We can also observe trends in the standard deviation, where there appears to be
a broad symmetry with regard to the length and width of each part of the flower. More detailed 
exploration below will provide further information and a deeper understanding.


**output (dependent variable sumary):**

```
                   Species Count
Species_A      Iris-setosa    50
Species_B  Iris-versicolor    50
Species_C   Iris-virginica    50
```




**note:** see *iris_summary.txt* to view formatted output

## Histogram

* Histograms are a useful way to visualise and assess the probability distribution of a data sample. [[8]](#8)
Python offers a number of different options to generate a histogram, from pure python to third party libraries
such as NumPy, Seaborn and Pandas. For this project, I decided to use Matplotlib. The `hist()` function is
simple to use, needing only one line of code to output an informative graphical representation. 

* To generate a histogram of each variable, I wrote two functions, both of which also save each figure as a 
png file. The first processes the numeric data:

``` python
def var_hist(var_data, fig_num, x_label, y_label, title, filepath):
    plt.figure(fig_num)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.hist(var_data, rwidth=0.9,)
    plt.savefig(filepath)
    plt.close() # Close figure so plot won't be displayed later


# Call function for each variable
var_hist(sep_len, 1, 'sepal_length_cm', 'Frequency', 'Sepal Length', 'sepal_length.png')
var_hist(sep_width, 2, 'sepal_width_cm', 'Frequency', 'Sepal Width', 'sepal_width.png')
var_hist(pet_len, 3, 'petal_length_cm', 'Frequency', 'Petal Length', 'petal_length.png')
var_hist(pet_width, 4, 'petal_width_cm', 'Frequency', 'Petal Width', 'petal_width.png')
```

**Output**:

![Sepal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/sepal_length.png)
![Sepal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/sepal_width.png)
![Petal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/petal_length.png)
![Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/petal_width.png)


* The second function is almost identical and generates a histogram representing the
3 unique values of the target variable (see *analysis.py*). Graphical representation of this variable does not
give us any additional information. It can be viewed in this repository (see *species.png*) 

* Comparison between each variable is easier when viewed as 4 separate axes on a single figure:

```python
# 4 axes on one figure for better visual comparison
fig, axs = plt.subplots(2, 2)

axs1 = axs[0, 0]
axs1.hist(sep_len, rwidth=0.9)
axs1.set_title('Sepal_Length_Cm')
axs1.set(ylabel='frequency')

axs2 = axs[0, 1]
axs2.hist(sep_width, rwidth=0.9)
axs2.set_title('Sepal_Width_Cm')
axs2.set(ylabel='frequency')

axs3 = axs[1, 0]
axs3.hist(pet_len, rwidth=0.9)
axs3.set_title('Petal_Length_Cm')
axs3.set(ylabel='frequency')

axs4 = axs[1, 1]
axs4.hist(pet_width, rwidth=0.9)
axs4.set_title('Petal_Width_Cm')
axs4.set(ylabel='frequency')

plt.show()
```

![4 Histograms](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/4_hist.png)

These histograms give us a clearer picture of the distribution of each attribute, building on the information extracted 
from the summary. I have used the default binning strategy (10 bins) however 
Matplotlib's `hist()` function provides the option of additional binning strategies such as 'auto', 'sturges',
'doane' etc. These refer to alternative formulas which offer a different perspective on the data. 
(see Matplotlib [documentation](https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.hist.html))


## Scatter plot
* A scatter plot shows the relationship between two variables in a dataset by plotting each 
observation and representing them as dots. The resulting patterns can be very informative,
"... [indicating] the type and strength of the relationship between the two variables." [[9]](#9)

* I initially generated scatter plots using Matpotlib's `scatter()` function. However, while the 
pattern is informative and does highlight trends in the data, it does not distinguish between
the categorical variables and so does not tell us the whole story:

![Scatter_1](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/matplotlib_scatter.png)

* With Matplotlib, distinguishing each categorical variable by colour involves a number of steps. This
function is based on solutions I found on stackoverflow.com [[10]](#10). The dictionary `colordict` is defined and maps
the `species` colours to the plotting colours:


```python
# Function to assign colour to each target variable 
def irisScatter(data1, data2, catcol):
    categories = np.unique(catcol)
    colors = np.linspace(0, 1, len(categories))
    colordict = dict(zip(categories, colors))
    catcol = catcol.apply(lambda x: colordict[x])
    fig = plt.scatter(data1, data2, c=catcol)
    return fig

# Call function
irisScatter(sep_len, sep_width, species)
```

* Seaborn offers a much neater option to do this with the `hue` parameter in the `lmplot()` function:

```python
# Write a function which outputs a scatter plot of each pair of variables.
# Each categorical variable (species of iris flower) is categorized by colour
def scatter(x, y):
    sns.set(style="darkgrid")
    sns.lmplot(x, y, iris_data, fit_reg=False, hue='species')
    plt.show()
    plt.close()

    
# Call function for each pair of variables
scatter('sepal_length', 'sepal_width')
scatter('sepal_length', 'petal_length')
scatter('sepal_length', 'petal_width')
scatter('sepal_width', 'petal_length')
scatter('sepal_width', 'petal_width')
scatter('petal_length', 'petal_width')
```

**Output:**

![Sepal Length, Sepal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/scatterA.png)
![Sepal Length, Petal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/scatterB.png)
![Sepal Length, Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/scatterC.png)
![Sepal Width, Petal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/scatterD.png)
![Sepal Width, Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/scatterE.png)
![Petal Length, Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/scatterF.png) 

* When separated by colour, each species in the data set is visibly distinguishable. The setosa in particular has 
characteristics which clearly mark it out from the the virginica and the versicolor, regardless of which two 
variables are plotted. 


**Note:** There is quite a lot of discussion around the benefits of certain visualisation tools relative to others.
Python offers a wide range of options through third party libraries and each has its merits depending on what
one wants to achieve. The blog posts [here](https://towardsdatascience.com/matplotlib-vs-seaborn-vs-plotly-f2b79f5bddb)
and [here](https://blog.magrathealabs.com/choosing-one-of-many-python-visualization-tools-7eb36fa5855f) helped
to steer me in the right direction. 


## Pairplot
* Seaborn's `pairplot()` function allows us to view joint (scatter plots) and marginal (histogram or kde) distribution 
in a single figure, using minimal lines of code:

```python
# Output pairplot using kde to represent marginal distribution
sns.set(style='ticks', color_codes=True)
sns.pairplot(iris_data, hue='species', diag_kind='kde')
plt.show()
```

**Output:**

![Pairplot](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/pairplot.png)

* From this we get an insightful overview of the data set, combining the various plots used in this project into one
single figure. The KDE (Kernal Density Estimation) serves as "... a way to estimate the probability density 
function of a continuous random variable" [[11]](#11).

## References
<b id="1">[1]</b>
UCI Machine Learning Repository, Iris Data Set: https://archive.ics.uci.edu/ml/datasets/Iris  
<b id="2">[2]</b>
geeksforgeeks.org, "Numpy in Python | Set 1 (introduction)": https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/  
SciPy.org, "What is NumPy?": https://docs.scipy.org/doc/numpy/user/whatisnumpy.html  
medium.com, "Why should we use NumPy?": https://medium.com/fintechexplained/why-should-we-use-numpy-c14a4fb03ee9  
<b id="3">[3]</b>
learnpython.org, "Pandas Basics": https://www.learnpython.org/en/Pandas_Basics  
<b id="4">[4]</b>
matplotlib.org, "Third Party Packages": https://matplotlib.org/thirdpartypackages/index.html  
realpython.com, "Python Plotting with Matplotlib (Guide)": https://realpython.com/python-matplotlib-guide/  
<b id="5">[5]</b>
pydata.org, "Seaborn: Statistical Data Visualization": https://seaborn.pydata.org/  
<b id="6"[6]</b>
Brownlee, J., 2018, "How to Calculate the 5-Number Summary for Your Data in Python": https://machinelearningmastery.com/how-to-calculate-the-5-number-summary-for-your-data-in-python/  
<b id="7"[7]</b>
geeksforgeeks.org, "Python | Pandas Dataframe.describe() method": https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/  
<b id="8"[8]</b>
realpython.com, "Python Histogram Plotting: NumPy, Matplotlib, Pandas & Seaborn": https://realpython.com/python-histograms/  
<b id="9"[9]</b>
yale.edu, "Scatterplot": http://www.stat.yale.edu/Courses/1997-98/101/scatter.htm  
<b id="10"[10]</b>
https://stackoverflow.com/questions/26139423/plot-different-color-for-different-categorical-levels-using-matplotlib  
https://stackoverflow.com/questions/14885895/color-by-column-values-in-matplotlib  
<b id="11"[11]</b>
tutorialspoint.com, "Seaborn - Kernel Density Estimates": https://www.tutorialspoint.com/seaborn/seaborn_kernel_density_estimates.htm  
