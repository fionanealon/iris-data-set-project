# Fiona Nealon, 2018-04-19
# Iris data set analysis

# Calculate the mean of each column in the numpy array

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

# Find the median of the first column of data
meanfirstcol = numpy.mean(firstcol)
# Find the median of the second column of data
meansecondcol = numpy.mean(secondcol)
# Find the median of the third column of data
meanthirdcol = numpy.mean(thirdcol)
# Find the median of the fourth column of data
meanfourthcol = numpy.mean(fourthcol)

# Print the median of the first column 
print("Mean of first column is:", meanfirstcol)
# Print the median of the second column 
print("Mean of second column is:", meansecondcol)
# Print the median of the third column 
print("Mean of third column is:", meanthirdcol)
# Print the median of the foruth column 
print("Mean of fourth column is:", meanfourthcol)