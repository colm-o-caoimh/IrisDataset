# PAS2020_project
Final project Programming and Scripting 2020

## Introduction
* In this project I investigate the famous Iris data set using Python. The text editor I used is Visual 
Studio Code.

## Data search and download
* Following a simple Google search, one quickly establishes that the Iris data set is used widely
in the fields of machine learning and statistics. It is referenced in
numerous academic publications, student projects, online tutorials etc. so there
is no shortage of sources offering the file for download. The most commonly 
referenced source appeared to be the UCI (University of California Irvine) [website](https://archive.ics.uci.edu/ml/datasets/Iris),
whose machine learning repository offers the data set for download, amongst many others.
It is this source that I have used in this project.

* It is important to mention that the UCI data set differs slightly from the data 
presented in Fisher's original paper. This is noted in the dataset documentation.

## Iris data set
* The data was collected by Edgar Anderson and introduced by Ronald A. Fisher in his
paper "The use of multiple measurements in taxonomic problems" in 1936. According
to the UCI website, the paper "... is a classic in the field [of pattern recognition]
and is referenced frequently to this day" **(REF)**

* A multivariate data set, it contains a total of 150 instances consisting of 50 instances
of each of 3 classes: *Iris-setosa*, *Iris-virginica* and *Iris-versicolor*. These refer
to 3 different species of the iris flower. There are 4 attributes in the sample: *sepal length*,
*sepal width*, *petal length* and *petal width*, referring to the parts of each flower
measured by Anderson.

## Python Libraries
**NumPy**: NumPy is roundly described as the fundamental package for scientific computing
and data analysis with Python **(REF)**. Among numerous other important features it contains,
NumPy's ndarray object allows for vectorized mathematical operations which is essential for 
any investigation and analysis of data.

**Pandas**: Pandas is built on the NumPy package and is a high-level data manipulation tool (**REF**).
The key data structure associated with Pandas is the DataFrame, which orders data in tables of
rows (observations) and columns (variables).

**Matplotlib.pyplot**: For data visualisation, Matplotlib is the fundamental library for the
Python programming language. It provides the underlying structure for many other visualisation libraries
in Python e.g. Seaborn, Holoviews. (**REF**) The pyplot module is used in this project for the generation
of histograms to investigate each variable in the data set.

**Seaborn**: Seaborn is built on Matplotlib and provides a "... high level interface for drawing
statistical graphics..." It uses much fewer lines of code for certain plot types, when compared
with Matplotlib, which can be quite verbose. In this project I have utlised Seaborn for the 
purpose of generating insightful scatter plots with minimal lines of code. 

## Importing the data
* Initial attempts to import the data involved using NumPy's `loadtxt()` and `genfromtxt()` functions.
However I eventually used Pandas to load the data for analysis:

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
in the analysis of a data set **(REF)**. It involves calculating the minimum, 1st quartile, 
median, 3rd quartile and maximum of a data set in order to describe its distribution.

* I first grouped the variables according to data type:

```python
# Isolate columns according to data type
float_values = iris_data.iloc[:,0:4]
str_values = iris_data.iloc[:,4]
```

* For the numeric data, I initially calculated each statistic using the `max()`, `min()` and `median()` functions before 
applying NumPy's `percentile()` function to the data. I subsequently discovered Pandas `describe()`
function **(REF)** which outputs a DataFrame containing the relevant statistical information:

```python
# Use describe function to summarise data
float_summary = float_values.describe()
str_summary = str_values.describe()
```

**Output:**

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


* For the dependent variable summary, I used `describe()` once more. A number of additional steps
were needed to output the information in the same tabular format as above (see *analysis.py*). 
`str_summary.unique()` creates an `nparray` of each of target variable. This array was then 
converted to a DataFrame to get the desired format for output:

```
                   Species Count
Species_A      Iris-setosa    50
Species_B  Iris-versicolor    50
Species_C   Iris-virginica    50
```

* The summary output was further formatted and written to a txt file. (see *iris_summary.txt*)

## Histogram

* Histograms are a useful way to visualise and assess the probability distribution of a data sample. **(REF)**
Python offers a number of different options to generate a histogram, from pure python to third party libraries
such as NumPy, Seaborn and Pandas. For this project, I decided to use Matplotlib. The `hist()` function is
simple to use, needing only one line of code to output an informative graphical representation. 

* To generate a histogram of each variable, I wrote two functions, both of which also save each figure as a 
png file. The first processes the numeric data:

**note:** I have used the default binning strategy (10 bins) however 
Matplotlib's `hist()` function provides the option of additional binning strategies such as 'auto', 'sturges',
'doane' etc. These refer to alternative formulas which offer a different perspective on the data. 
(see Matplotlib [documentation](https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.hist.html))

``` python
def var_hist(var_data, fig_num, x_label, y_label, title, filepath):
    plt.figure(fig_num)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.hist(var_data, rwidth=0.9,)
    plt.savefig(filepath)
    plt.close() # Close figure so plot won't be displayed later
```

This function outputs the following histograms:

![Sepal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/sepal_length.png)
![Sepal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/sepal_width.png)
![Petal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/petal_length.png)
![Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/petal_width.png)


The second function is almost identical and generates a histogram representing the
3 unique values of the target variable (see *analysis.py*):

![Species](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/species.png)

* Comparison between each variable is easier when viewed as 4 separate axes on a single figure:

![4 Histograms](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/4_hist.png)



## Scatter plot
* A scatter plot shows the relationship between two variables in a dataset by plotting each 
observation and representing them as dots. The resulting patterns can be very informative,
"... [indicating] the type and strength of the relationship between the two variables." **(REF)**

* I initially generated scatter plots using Matpotlib's `scatter()` function. However, while the 
pattern is informative, highlighting trends in the data, it does not distinguish between
the categorical variables and so does not tell us the whole story:

![Scatter_1](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/scatter1.png)

* With Matplotlib, distinguishing each categorical variable by colour involves a number of steps. This
function is based on a solution I found here **(REF)**:


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
def scatter(x, y, filepath):
    sns.set(style="darkgrid")
    sns.lmplot(x, y, iris_data, fit_reg=False, hue='species')
    plt.show()
    plt.savefig(filepath)
    plt.close()
```

**Output:**

![Sepal Length, Sepal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/fig1.png)
![Sepal Length, Petal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/fig.png)
![Sepal Length, Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/fig3.png)
![Sepal Width, Petal Length](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/fig4.png)
![Sepal Width, Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/fig5.png)
![Petal Length, Petal Width](https://github.com/colm-o-caoimh/PAS2020_project/blob/master/image_uploads/fig6.png) 

**Note:** There is quite a lot of discussion around the benefits of certain visualisation tools relative to others.
Python offers a wide range of options through third party libraries and each has its merits depending on what
one wants to achieve. The blog posts [here](https://towardsdatascience.com/matplotlib-vs-seaborn-vs-plotly-f2b79f5bddb)
and [here](https://blog.magrathealabs.com/choosing-one-of-many-python-visualization-tools-7eb36fa5855f) helped
to steer me in the right direction. 


## Pairplot
* Seaborn's `pairplot()` function generates a plot 




