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

# Find the median of the first column of data
medianfirstcol = numpy.median(firstcol)
# Find the median of the second column of data
mediansecondcol = numpy.median(secondcol)
# Find the median of the third column of data
medianthirdcol = numpy.median(thirdcol)
# Find the median of the fourth column of data
medianfourthcol = numpy.median(fourthcol)

# Print the median of the first column 
print("Median of first column is:", medianfirstcol)
# Print the median of the second column 
print("Median of second column is:", mediansecondcol)
# Print the median of the third column 
print("Median of third column is:", medianthirdcol)
# Print the median of the foruth column 
print("Median of fourth column is:", medianfourthcol)