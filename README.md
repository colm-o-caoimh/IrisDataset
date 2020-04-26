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
referenced source appeared to be the UCI (University of California Irvine) website,
whose machine learning repository offers the data set for download, amongst many others.
It is this source that I have used in this project.

* It is important to mention that the UCI data set differs slightly from the data 
presented in Fisher's original paper. This is noted in the dataset documentation.

## Iris data set
* The data was collected by Edgar Anderson and introduced by Ronald A. Fisher in his
paper "The use of multiple measurements in taxonomic problems" in 1936. According
to the UCI website, the paper "... is a classic in the field [of pattern recognition]
and is referenced frequently to this day"

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

This imports the data as a DataFrame which enables easier manipulation throughout the program.





