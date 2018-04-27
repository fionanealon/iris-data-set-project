# Project 2018

## Problem statement

The following project concerns the well-known Fischer's Iris data set. The project entails you reseacrhing the data set, and then writing documentation and code in the Python programming language based on that research.

An online search for information on the data set will convince you that many people have investigated and written about it previously, and may of those are not experienced programmers, You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed. You might do that for this project as follows:

**1. Research back ground information about the data set and write a summary about it.**


![A picture of fischer](Fischer.jpg)

One of the first multivariate data sets was introduced by British statiscian and biologist Ronald Fischer in 1936. This was named the Iris flower data set or Fisher's Iris data set. It is sometimes referred to as Anderson's Iris data set as it was Edgar Anderson who collected the data to quantify the morphologic variation of Iris flowers of three related species. There are 150 rows of data in the dataet and each row of the dataset represents an iris flower, including its species and dimensions of its botanical parts, sepal and petal, in centimeters. [Ref: Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

![A picture of iris](iris.png)

The above picture shows the three species contained in each class of the dataset - Iris setosa, Iris virginica and Iris versicolor. The dataset contains 50 samples each of these species with their botanical dimensions, sepal and petal, included in each row of the dataset.

![A picture of iris labels](iris_with_labels.jpg)

Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. The sepal is described as a part of the flower of angiosperms (flowering plants). Sepals typically function as protection for the flower in bud, and often as support for the petals when in bloom. [Ref: Sepal](https://en.wikipedia.org/wiki/Sepal) Petals are described as modified leaves that surround the reproductive parts of flowers. [Ref: Petal](https://en.wikipedia.org/wiki/Petal) 

![A picture of machine learning](vPTf6.png)

Although Fischer's Iris flower data set was initially compiled to identify the botanical variations of Iris flowers, it has since become a famous data set for testing purposes in the computer science world. [Ref: alternative uses](https://www.techopedia.com/definition/32880/iris-flower-data-set)It a well known, standard data set which programmers repeatedly use as an input to examine how various technologies sort and handle data sets. It is also used for testing out machine learning algorithms and visualizations (for example, Scatter Plot, Histogram). The above shows an expample of how the Iris flower data set is used in machine learning algorithms. [Ref: Machine learning algorithms](https://stats.stackexchange.com/questions/268561/example-of-backpropagation-for-neural-network-with-softmax-and-sigmoid-activatio)

**2. Keep a list of references you used in completing the project.**

https://en.wikipedia.org/wiki/Iris_flower_data_set
https://en.wikipedia.org/wiki/Petal
https://en.wikipedia.org/wiki/Sepal)
https://www.techopedia.com/definition/32880/iris-flower-data-set
https://en.wikipedia.org/wiki/NumPy
https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html?highlight=array
https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php
https://stats.stackexchange.com/questions/268561/example-of-backpropagation-for-neural-network-with-softmax-and-sigmoid-activatio


**3. Download the data set and write some Python code to investigate it**


**4. Summarise the data set by, for example calculating the maximun, minimum and mean of each column. A Pythin script will quickly do this for you.

#### Mean of each column in the Iris flower data set

The mean is the average of an array of numbers. It is calculated by summing all of the numbers in the array and then dividing by the total count of numbers.

```Python
# Fiona Nealon, 2018-04-19
# Iris data set analysis

# Calculate the mean of each column in the numpy array

# Use numpy library to analyse Iris file
import numpy
```

The numpy library provides some advanced math functionalities to python. It adds support for large multi-dimensional arrays and provides a collection of high level mathematical functions to operate on these arrays to assist in manipulating numerical data. I will use the numpy.genfromtxt and the numpy.mean functions to read the csv file into python using numpy and calculate the mean of each column in the Iris flower data set. [Ref: numpy](https://en.wikipedia.org/wiki/NumPy)


```Python
# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
```
Using the numpy.genfromtxt function, I will use numpy to read in the iris csv file into this array and assign this array to data. The numpy.genfromtxt function runs two main loops. The first loop converts each line of the file in a sequence of strings. The second loop converts each string to the appropriate data type. [Ref: numpy.genfromtxt](https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html?highlight=array) A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. [Ref: delimiter](https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php)

```Python
# Select all values in first column of numpy array
firstcol = data[:,0]
# Select all values in second column of numpy array
secondcol = data[:,1]
# Select all values in third column of numpy array
thirdcol = data[:,2]
# Select all values in fourth column of numpy array
fourthcol = data[:,3]
```
In the next block of code, I will assign values to the 1st, 2nd, 3rd and 4th columns in the numpy array. Data is a two dimensional array - an array of arrays. ```python Data[0]``` is the usual way to access first element in a list or array. In this case, this will only return the first row of the data. However, I also require the first column of data. To select all of the values in a column in a numpy array, I need to adding the following code ```python :,``` to my code so that this selects everything in the first dimension of the array (the column). ```python Data[0]``` represents the second dimension of the array. I can adjust the index method in my code and apply the same logic to select the second, third and fourth columns of the numpy array.

```Python
# Find the average of the first column of data
meanfirstcol = numpy.mean(firstcol)
# Find the average of the second column of data
meansecondcol = numpy.mean(secondcol)
# Find the average of the third column of data
meanthirdcol = numpy.mean(thirdcol)
# Find the average of the fourth column of data
meanfourthcol = numpy.mean(fourthcol)
```
Using the above block of code, the numpy.mean function calls the values assigned to firstcol, secondcol, thirdcol & fourthcol and calulates the average of each of the columns. The mean value of each of the columns is then assigned to meanfirstcol, meansecondcol, meanthirdcol & meanfourthcol.

```Python
# Print the average of the first column 
print("Average of first column is:", meanfirstcol)
# Print the average of the second column 
print("Average of second column is:", meansecondcol)
# Print the average of the third column 
print("Average of third column is:", meanthirdcol)
# Print the average of the fourth column 
print("Average of fourth column is:", meanfourthcol)
```
Python then makes call to the values assigned to meanfirstcol, meansecondcol, meanthirdcol and meanfourthcol, I have added a string to the code to explain these values and they are then printed them to the command prompt.

#### Maximum of each column in the Iris flower data set

The maximum number is the largest number in an array of numbers. This python script uses a similar logic to the logic used to calculate the mean of each of the columns in the Iris Flower data set.

```Python
# Fiona Nealon, 2018-04-25
# Iris data set analysis

# Calculate the maximum of each column in the numpy array

# Use numpy library to analyse Iris file
import numpy
```

The numpy library provides some advanced math functionalities to python. It adds support for large multi-dimensional arrays and provides a collection of high level mathematical functions to operate on these arrays to assist in manipulating numerical data. I will use the numpy.genfromtxt and the numpy.mean functions to read the csv file into python using numpy and calculate the mean of each column in the Iris flower data set. [Ref: numpy](https://en.wikipedia.org/wiki/NumPy)


```Python
# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
```
Using the numpy.genfromtxt function, I will use numpy to read in the iris csv file into this array and assign this array to data. The numpy.genfromtxt function runs two main loops. The first loop converts each line of the file in a sequence of strings. The second loop converts each string to the appropriate data type. [Ref: numpy.genfromtxt](https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html?highlight=array) A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. [Ref: delimiter](https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php)

```Python
# Select all values in first column of numpy array
firstcol = data[:,0]
# Select all values in second column of numpy array
secondcol = data[:,1]
# Select all values in third column of numpy array
thirdcol = data[:,2]
# Select all values in fourth column of numpy array
fourthcol = data[:,3]
```
In the next block of code, I will assign values to the 1st, 2nd, 3rd and 4th columns in the numpy array. Data is a two dimensional array - an array of arrays. ```python Data[0]``` is the usual way to access first element in a list or array. In this case, this will only return the first row of the data. However, I also require the first column of data. To select all of the values in a column in a numpy array, I need to adding the following code ```python :,``` to my code so that this selects everything in the first dimension of the array (the column). ```python Data[0]``` represents the second dimension of the array. I can adjust the index method in my code and apply the same logic to select the second, third and fourth columns of the numpy array.

```Python
maxfirstcol = numpy.max(firstcol)
# Find the maximum of the second column of data
maxsecondcol = numpy.max(secondcol)
# Find the maximum of the third column of data
maxthirdcol = numpy.max(thirdcol)
# Find the maximum of the fourth column of data
maxfourthcol = numpy.max(fourthcol)
```
Using the above block of code, the numpy.max function calls the values assigned to firstcol, secondcol, thirdcol & fourthcol and calulates the maximum of each of the columns. The maximum value of each of the columns is then assigned to maxfirstcol, maxsecondcol, maxthirdcol & maxfourthcol.

```Python
# Print the maximum of the first column 
print("Maximum of first column is:", maxfirstcol)
# Print the maximum of the second column 
print("Maximum of second column is:", maxsecondcol)
# Print the maximum of the third column 
print("Maximum of third column is:", maxthirdcol)
# Print the maximum of the fourth column 
print("Maximum of fourth column is:", maxfourthcol)
```
Python then makes call to the values assigned to maxfirstcol, maxsecondcol, maxthirdcol and maxfourthcol, I have added a string to the code to explain these values and they are then printed them to the command prompt.

#### Minimum of each column in the Iris flower data set

The minimum number is the smallest number in an array of numbers. This python script uses a similar logic to the logic used to calculate the mean of each of the columns in the Iris Flower data set.

```Python
# Fiona Nealon, 2018-04-1925
# Iris data set analysis

# Calculate the median of each column in the numpy array

# Use numpy library to analyse Iris file
import numpy
```

The numpy library provides some advanced math functionalities to python. It adds support for large multi-dimensional arrays and provides a collection of high level mathematical functions to operate on these arrays to assist in manipulating numerical data. I will use the numpy.genfromtxt and the numpy.mean functions to read the csv file into python using numpy and calculate the mean of each column in the Iris flower data set. [Ref: numpy](https://en.wikipedia.org/wiki/NumPy)


```Python
# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
```
Using the numpy.genfromtxt function, I will use numpy to read in the iris csv file into this array and assign this array to data. The numpy.genfromtxt function runs two main loops. The first loop converts each line of the file in a sequence of strings. The second loop converts each string to the appropriate data type. [Ref: numpy.genfromtxt](https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html?highlight=array) A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. [Ref: delimiter](https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php)

```Python
# Select all values in first column of numpy array
firstcol = data[:,0]
# Select all values in second column of numpy array
secondcol = data[:,1]
# Select all values in third column of numpy array
thirdcol = data[:,2]
# Select all values in fourth column of numpy array
fourthcol = data[:,3]
```
In the next block of code, I will assign values to the 1st, 2nd, 3rd and 4th columns in the numpy array. Data is a two dimensional array - an array of arrays. ```python Data[0]``` is the usual way to access first element in a list or array. In this case, this will only return the first row of the data. However, I also require the first column of data. To select all of the values in a column in a numpy array, I need to adding the following code ```python :,``` to my code so that this selects everything in the first dimension of the array (the column). ```python Data[0]``` represents the second dimension of the array. I can adjust the index method in my code and apply the same logic to select the second, third and fourth columns of the numpy array.

```Python
# Find the minimum of the first column of data
minfirstcol = numpy.min(firstcol)
# Find the minimum of the second column of data
minsecondcol = numpy.min(secondcol)
# Find the minimum of the third column of data
minthirdcol = numpy.min(thirdcol)
# Find the minimum of the fourth column of data
minfourthcol = numpy.min(fourthcol)
```
Using the above block of code, the numpy.max function calls the values assigned to firstcol, secondcol, thirdcol & fourthcol and calulates the maximum of each of the columns. The maximum value of each of the columns is then assigned to minfirstcol, minsecondcol, minthirdcol & minfourthcol.

```Python
# Print the minimum of the first column
print("Minimum of first column is:", minfirstcol)
# Print the minimum of the second column
print("Minimum of second column is:", minsecondcol)
# Print the minimum of the third column
print("Minimum of third column is:", minthirdcol)
# Print the minimum if the fourth column
print("Minimum of fourth column is:", minfourthcol)
```
Python then makes call to the values assigned to minfirstcol, minsecondcol, minthirdcol and minfourthcol, I have added a string to the code to explain these values and they are then printed them to the command prompt.



# Plan for project

## Iris data set
- Research of Iris data set
- What it contains, what is it about?
- Background
- Why people talk about it so much in data analytics? Famous, standard data set
- How has it benefitted data analysis previously?

## Writing documentation in code in pythin programming language based on research. 
Code that does some preliminary investigation on the data
Summary statistics
- Columns
 - Max value in each column
 - Min value in each column
 - Mean/Average value in each column
 - Median value in each column
 - Spread in data/standard deviation
 - Plot a histogram
 - For loop (sum, average, max, min)
 
## References
Keep track of references. 20+ references


## Supporting Tables and graphs
- Tables in Markdown
- Histogram
- Matplotlib
- Graphics
- Scatterplots (what's a scatterplot, what do scatterplots do?)

## How to run python code

## Readme
- Summary of dataset & investigations
- Images, linnks, references


|sepal_length | sepal_width | petal_length | petal_width | species |
| --- | --- | --- | --- | --- |
5.1 | 3.5 | 1.4 | 0.2 | Iris-setosa
4.9 | 3.0 | 1.4 | 0.2 | Iris-setosa
4.7 | 3.2 | 1.3 | 0.2 | Iris-setosa
4.6 | 3.1 | 1.5 | 0.2 | Iris-setosa
5.0 | 3.6 | 1.4 | 0.2 | Iris-setosa
5.4 | 3.9 | 1.7 | 0.4 | Iris-setosa
4.6 | 3.4 | 1.4 | 0.3 | Iris-setosa
5.0 | 3.4 | 1.5 | 0.2 | Iris-setosa
4.4 | 2.9 | 1.4 | 0.2 | Iris-setosa
4.9 | 3.1 | 1.5 | 0.1 | Iris-setosa
5.4 | 3.7 | 1.5 | 0.2 | Iris-setosa
4.8 | 3.4 | 1.6 | 0.2 | Iris-setosa
4.8 | 3.0 | 1.4 | 0.1 | Iris-setosa
4.3 | 3.0 | 1.1 | 0.1 | Iris-setosa
5.8 | 4.0 | 1.2 | 0.2 | Iris-setosa
5.7 | 4.4 | 1.5 | 0.4 | Iris-setosa
5.4 | 3.9 | 1.3 | 0.4 | Iris-setosa
5.1 | 3.5 | 1.4 | 0.3 | Iris-setosa
5.7 | 3.8 | 1.7 | 0.3 | Iris-setosa
5.1 | 3.8 | 1.5 | 0.3 | Iris-setosa
5.4 | 3.4 | 1.7 | 0.2 | Iris-setosa
5.1 | 3.7 | 1.5 | 0.4 | Iris-setosa
4.6 | 3.6 | 1.0 | 0.2 | Iris-setosa
5.1 | 3.3 | 1.7 | 0.5 | Iris-setosa
4.8 | 3.4 | 1.9 | 0.2 | Iris-setosa
5.0 | 3.0 | 1.6 | 0.2 | Iris-setosa
5.0 | 3.4 | 1.6 | 0.4 | Iris-setosa
5.2 | 3.5 | 1.5 | 0.2 | Iris-setosa
5.2 | 3.4 | 1.4 | 0.2 | Iris-setosa
4.7 | 3.2 | 1.6 | 0.2 | Iris-setosa
4.8 | 3.1 | 1.6 | 0.2 | Iris-setosa
5.4 | 3.4 | 1.5 | 0.4 | Iris-setosa
5.2 | 4.1 | 1.5 | 0.1 | Iris-setosa
5.5 | 4.2 | 1.4 | 0.2 | Iris-setosa
4.9 | 3.1 | 1.5 | 0.1 | Iris-setosa
5.0 | 3.2 | 1.2 | 0.2 | Iris-setosa
5.5 | 3.5 | 1.3 | 0.2 | Iris-setosa
4.9 | 3.1 | 1.5 | 0.1 | Iris-setosa
4.4 | 3.0 | 1.3 | 0.2 | Iris-setosa
5.1 | 3.4 | 1.5 | 0.2 | Iris-setosa
5.0 | 3.5 | 1.3 | 0.3 | Iris-setosa
4.5 | 2.3 | 1.3 | 0.3 | Iris-setosa
4.4 | 3.2 | 1.3 | 0.2 | Iris-setosa
5.0 | 3.5 | 1.6 | 0.6 | Iris-setosa
5.1 | 3.8 | 1.9 | 0.4 | Iris-setosa
4.8 | 3.0 | 1.4 | 0.3 | Iris-setosa
5.1 | 3.8 | 1.6 | 0.2 | Iris-setosa
4.6 | 3.2 | 1.4 | 0.2 | Iris-setosa
5.3 | 3.7 | 1.5 | 0.2 | Iris-setosa
5.0 | 3.3 | 1.4 | 0.2 | Iris-setosa
7.0 | 3.2 | 4.7 | 1.4 | Iris-versicolor
6.4 | 3.2 | 4.5 | 1.5 | Iris-versicolor
6.9 | 3.1 | 4.9 | 1.5 | Iris-versicolor
5.5 | 2.3 | 4.0 | 1.3 | Iris-versicolor
6.5 | 2.8 | 4.6 | 1.5 | Iris-versicolor
5.7 | 2.8 | 4.5 | 1.3 | Iris-versicolor
6.3 | 3.3 | 4.7 | 1.6 | Iris-versicolor
4.9 | 2.4 | 3.3 | 1.0 | Iris-versicolor
6.6 | 2.9 | 4.6 | 1.3 | Iris-versicolor
5.2 | 2.7 | 3.9 | 1.4 | Iris-versicolor
5.0 | 2.0 | 3.5 | 1.0 | Iris-versicolor
5.9 | 3.0 | 4.2 | 1.5 | Iris-versicolor
6.0 | 2.2 | 4.0 | 1.0 | Iris-versicolor
6.1 | 2.9 | 4.7 | 1.4 | Iris-versicolor
5.6 | 2.9 | 3.6 | 1.3 | Iris-versicolor
6.7 | 3.1 | 4.4 | 1.4 | Iris-versicolor
5.6 | 3.0 | 4.5 | 1.5 | Iris-versicolor
5.8 | 2.7 | 4.1 | 1.0 | Iris-versicolor
6.2 | 2.2 | 4.5 | 1.5 | Iris-versicolor
5.6 | 2.5 | 3.9 | 1.1 | Iris-versicolor
5.9 | 3.2 | 4.8 | 1.8 | Iris-versicolor
6.1 | 2.8 | 4.0 | 1.3 | Iris-versicolor
6.3 | 2.5 | 4.9 | 1.5 | Iris-versicolor
6.1 | 2.8 | 4.7 | 1.2 | Iris-versicolor
6.4 | 2.9 | 4.3 | 1.3 | Iris-versicolor
6.6 | 3.0 | 4.4 | 1.4 | Iris-versicolor
6.8 | 2.8 | 4.8 | 1.4 | Iris-versicolor
6.7 | 3.0 | 5.0 | 1.7 | Iris-versicolor
6.0 | 2.9 | 4.5 | 1.5 | Iris-versicolor
5.7 | 2.6 | 3.5 | 1.0 | Iris-versicolor
5.5 | 2.4 | 3.8 | 1.1 | Iris-versicolor
5.5 | 2.4 | 3.7 | 1.0 | Iris-versicolor
5.8 | 2.7 | 3.9 | 1.2 | Iris-versicolor
6.0 | 2.7 | 5.1 | 1.6 | Iris-versicolor
5.4 | 3.0 | 4.5 | 1.5 | Iris-versicolor
6.0 | 3.4 | 4.5 | 1.6 | Iris-versicolor
6.7 | 3.1 | 4.7 | 1.5 | Iris-versicolor
6.3 | 2.3 | 4.4 | 1.3 | Iris-versicolor
5.6 | 3.0 | 4.1 | 1.3 | Iris-versicolor
5.5 | 2.5 | 4.0 | 1.3 | Iris-versicolor
5.5 | 2.6 | 4.4 | 1.2 | Iris-versicolor
6.1 | 3.0 | 4.6 | 1.4 | Iris-versicolor
5.8 | 2.6 | 4.0 | 1.2 | Iris-versicolor
5.0 | 2.3 | 3.3 | 1.0 | Iris-versicolor
5.6 | 2.7 | 4.2 | 1.3 | Iris-versicolor
5.7 | 3.0 | 4.2 | 1.2 | Iris-versicolor
5.7 | 2.9 | 4.2 | 1.3 | Iris-versicolor
6.2 | 2.9 | 4.3 | 1.3 | Iris-versicolor
5.1 | 2.5 | 3.0 | 1.1 | Iris-versicolor
5.7 | 2.8 | 4.1 | 1.3 | Iris-versicolor
6.3 | 3.3 | 6.0 | 2.5 | Iris-virginica
5.8 | 2.7 | 5.1 | 1.9 | Iris-virginica
7.1 | 3.0 | 5.9 | 2.1 | Iris-virginica
6.3 | 2.9 | 5.6 | 1.8 | Iris-virginica
6.5 | 3.0 | 5.8 | 2.2 | Iris-virginica
7.6 | 3.0 | 6.6 | 2.1 | Iris-virginica
4.9 | 2.5 | 4.5 | 1.7 | Iris-virginica
7.3 | 2.9 | 6.3 | 1.8 | Iris-virginica
6.7 | 2.5 | 5.8 | 1.8 | Iris-virginica
7.2 | 3.6 | 6.1 | 2.5 | Iris-virginica
6.5 | 3.2 | 5.1 | 2.0 | Iris-virginica
6.4 | 2.7 | 5.3 | 1.9 | Iris-virginica
6.8 | 3.0 | 5.5 | 2.1 | Iris-virginica
5.7 | 2.5 | 5.0 | 2.0 | Iris-virginica
5.8 | 2.8 | 5.1 | 2.4 | Iris-virginica
6.4 | 3.2 | 5.3 | 2.3 | Iris-virginica
6.5 | 3.0 | 5.5 | 1.8 | Iris-virginica
7.7 | 3.8 | 6.7 | 2.2 | Iris-virginica
7.7 | 2.6 | 6.9 | 2.3 | Iris-virginica
6.0 | 2.2 | 5.0 | 1.5 | Iris-virginica
6.9 | 3.2 | 5.7 | 2.3 | Iris-virginica
5.6 | 2.8 | 4.9 | 2.0 | Iris-virginica
7.7 | 2.8 | 6.7 | 2.0 | Iris-virginica
6.3 | 2.7 | 4.9 | 1.8 | Iris-virginica
6.7 | 3.3 | 5.7 | 2.1 | Iris-virginica
7.2 | 3.2 | 6.0 | 1.8 | Iris-virginica
6.2 | 2.8 | 4.8 | 1.8 | Iris-virginica
6.1 | 3.0 | 4.9 | 1.8 | Iris-virginica
6.4 | 2.8 | 5.6 | 2.1 | Iris-virginica
7.2 | 3.0 | 5.8 | 1.6 | Iris-virginica
7.4 | 2.8 | 6.1 | 1.9 | Iris-virginica
7.9 | 3.8 | 6.4 | 2.0 | Iris-virginica
6.4 | 2.8 | 5.6 | 2.2 | Iris-virginica
6.3 | 2.8 | 5.1 | 1.5 | Iris-virginica
6.1 | 2.6 | 5.6 | 1.4 | Iris-virginica
7.7 | 3.0 | 6.1 | 2.3 | Iris-virginica
6.3 | 3.4 | 5.6 | 2.4 | Iris-virginica
6.4 | 3.1 | 5.5 | 1.8 | Iris-virginica
6.0 | 3.0 | 4.8 | 1.8 | Iris-virginica
6.9 | 3.1 | 5.4 | 2.1 | Iris-virginica
6.7 | 3.1 | 5.6 | 2.4 | Iris-virginica
6.9 | 3.1 | 5.1 | 2.3 | Iris-virginica
5.8 | 2.7 | 5.1 | 1.9 | Iris-virginica
6.8 | 3.2 | 5.9 | 2.3 | Iris-virginica
6.7 | 3.3 | 5.7 | 2.5 | Iris-virginica
6.7 | 3.0 | 5.2 | 2.3 | Iris-virginica
6.3 | 2.5 | 5.0 | 1.9 | Iris-virginica
6.5 | 3.0 | 5.2 | 2.0 | Iris-virginica
6.2 | 3.4 | 5.4 | 2.3 | Iris-virginica
5.9 | 3.0 | 5.1 | 1.8 | Iris-virginica
