# Fiona Nealon, 2018-04-28
# Iris data set analysis
# Create a histogram for sepal length

# Use numpy library to analyse Iris file
import numpy

# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

# Select all values in first column of numpy array
firstcol = data[:,0]

# Use matplotlib & pyplot libraries to plot histogram
import matplotlib.pyplot as pl

# Plot histogram of the first column
pl.hist(firstcol)

# Add title to histogram
pl.title('sepal_length histogram')

# Output the histogram
pl.show()