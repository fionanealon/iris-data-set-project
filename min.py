# Fiona Nealon, 2018-04-19
# Iris data set analysis

# Calculate the median of each column in the numpy array

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
# Find the minimum of the first column of data
minfirstcol = numpy.min(firstcol)
# Find the minimum of the second column of data
minsecondcol = numpy.min(secondcol)
# Find the minimum of the third column of data
minthirdcol = numpy.min(thirdcol)
# Find the minimum of the fourth column of data
minfourthcol = numpy.min(fourthcol)

# Print the minimum of the first column
print("Minimum of first column is:", minfirstcol)
# Print the minimum of the second column
print("Minimum of second column is:", minsecondcol)
# Print the minimum of the third column
print("Minimum of third column is:", minthirdcol)
# Print the minimum if the fourth column
print("Minimum of fourth column is:", minfourthcol)
