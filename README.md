# Project 2018

## Problem statement

The following project concerns the well-known Fischer's Iris data set. The project entails you reseacrhing the data set, and then writing documentation and code in the Python programming language based on that research.

An online search for information on the data set will convince you that many people have investigated and written about it previously, and may of those are not experienced programmers, You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed. You might do that for this project as follows:

**1. Research back ground information about the data set and write a summary about it.**


![A picture of fischer](Fischer.jpg)

One of the first multivariate datasets was introduced by British statiscian and biologist Ronald Fischer in 1936. This was named the Iris flower data set or Fisher's Iris data set. It is sometimes referred to as Anderson's Iris data set as it was Edgar Anderson who collected the data to quantify the morphologic variation of Iris flowers of three related species. There are 150 rows of data in the dataet and each row of the dataset represents an iris flower, including its species and dimensions of its botanical parts, sepal and petal, in centimeters.

![A picture of iris](iris.png)

The above picture shows the three species contained in each class of the dataset - Iris setosa, Iris virginica and Iris versicolor. The dataset contains 50 samples each of these species with their botanical dimensions, sepal and petal, included in each row of the dataset.

![A picture of iris labels](iris_with_labels.jpg)

Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. The sepal is described as a part of the flower of angiosperms (flowering plants). Sepals typically function as protection for the flower in bud, and often as support for the petals when in bloom. Petals are described as modified leaves that surround the reproductive parts of flowers.

Although Fischer's Iris flower data set was initially collected to identify the botanical variations of Iris flowers, it has since become a famous data set for testing purposes in the computer science world. It a well known, standard data set which programmers repeatedly use as an input to examine how various technologies sort and handle data sets. It is also used for testing out machine learning algorithms and visualizations (for example, Scatter Plot, Histogram).

**2. Keep a list of references you used in completing the project.**

https://www.techopedia.com/definition/32880/iris-flower-data-set


**3. Download the data set and write some Python code to investigate it**


**4. Summarise the data set by, for example calculating the maximun, minimum and mean of each column. A Pythin script will quickly do this for you.

## Mean of each column in the Iris flower data set

```Python
# Fiona Nealon, 2018-04-19
# Iris data set analysis
# Calculate the mean of each column.

# Use numpy library to analyse Iris file
import numpy

# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

# Select all values in first column of numpy array
firstcol = data[:,0]
# Select all values in second column of numpy array
secondcol = data[:,1]
# Select all values in third column of numpy array
thirdcol = data[:,2]
# Select all values in fourth column of numpy array
fourthcol = data[:,3]
# Find the average of the first column of data
meanfirstcol = numpy.mean(data[:,0])
# Find the average of the second column of data
meansecondcol = numpy.mean(data[:,1])
# Find the average of the third column of data
meanthirdcol = numpy.mean(data[:,2])
# Find the average of the fourth column of data
meanfourthcol = numpy.mean(data[:,3])

# Print the average of the first column 
print("Average of first column is:", meanfirstcol)
# Print the average of the second column 
print("Average of second column is:", meansecondcol)
# Print the average of the third column 
print("Average of third column is:", meanthirdcol)
# Print the average of the fourth column 
print("Average of fourth column is:", meanfourthcol)
```



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
