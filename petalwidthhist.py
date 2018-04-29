# Fiona Nealon, 2018-04-28
# Iris data set analysis
# Create a histogram for petal width

# Use numpy library to analyse Iris file
import numpy

# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

# Select all values in fourth column of numpy array
fourthcol = data[:,3]

# Use matplotlib & pyplot libraries to plot histogram
import matplotlib.pyplot as pl

# Plot histogram of the fourth column
pl.hist(fourthcol)

# Add title to histogram
pl.title('petal_width histogram')

# Output the histogram
pl.show()