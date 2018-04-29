# Fiona Nealon, 2018-04-28
# Iris data set analysis
# Create a histogram for sepal width

# Use numpy library to analyse Iris file
import numpy

# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

# Select all values in second column of numpy array
secondcol = data[:,1]

# Use matplotlib & pyplot libraries to plot histogram
import matplotlib.pyplot as pl

# Plot histogram of the second column
pl.hist(secondcol)

# Add title to histogram
pl.title('sepal_width histogram')

# Output the histogram
pl.show()