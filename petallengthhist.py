# Fiona Nealon, 2018-04-28
# Iris data set analysis
# Create a histogram for petal length

# Use numpy library to analyse Iris file
import numpy

# Read csv file into python using numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

# Select all values in third column of numpy array
thirdcol = data[:,2]

# Use numatplotlib & pyplot libraries to plot histogram
import matplotlib.pyplot as pl

# Plot histogram of the third column
pl.hist(thirdcol)

# Add title to histogram
pl.title('petal_length histogram')

# Output the histogram
pl.show()