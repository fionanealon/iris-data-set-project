# Fiona Nealon, 2018-04-27
# Iris data set analysis
# A program to read it a .csv file and print max, min, sum, count & average of each column

# import pandas library
import pandas as pd
# Import numpy library
import numpy as np 


# Assign iris.csv file to dataset
dataset = pandas.read_csv('data/iris.csv')

# Get the maximum value of each column 
print('Maximum value of column sepal_length:', dataset['sepal_length'].max())
print('Maximum value of column sepal_length:', dataset['sepal_width'].max())
print('Maximum value of column sepal_length:', dataset['petal_length'].max())
print('Maximum value of column sepal_length:', dataset['petal_width'].max())

# Get the minimum value of each column
print('Minimum value of column sepal_length:', dataset['sepal_length'].min())
print('Minimum value of column sepal_length:', dataset['sepal_width'].min())
print('Minimum value of column sepal_length:', dataset['petal_length'].min())
print('Minimum value of column sepal_length:', dataset['petal_width'].min())

# Get the sum value of each column
print('Sum value of column sepal_length:', dataset['sepal_length'].sum())
print('Sum value of column sepal_length:', dataset['sepal_width'].sum())
print('Sum value of column sepal_length:', dataset['petal_length'].sum())
print('Sum value of column sepal_length:', dataset['petal_width'].sum())

# Get the count of the number of values of each column
print('Count of the number of values in column sepal_length:', dataset['sepal_length'].count())
print('Count of the number of values in column sepal_length:', dataset['sepal_width'].count())
print('Count of the number of values in sepal_length:', dataset['petal_length'].count())
print('Count of the number of values in sepal_length:', dataset['petal_width'].count())

# Get the average/mean of each column
print('The average of values in column sepal_length:', dataset['sepal_length'].mean())
print('The average of values in column sepal_length:', dataset['sepal_width'].mean())
print('The average of values in sepal_length:', dataset['petal_length'].mean())
print('The average of values in sepal_length:', dataset['petal_width'].mean())
