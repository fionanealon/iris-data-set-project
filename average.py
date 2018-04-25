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
