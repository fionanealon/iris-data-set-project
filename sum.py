# Fiona Nealon, 2018-04-26
# Iris data set analysis

# Calculate the sum of each column in the numpy array
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
# Find the sum of the first column of data
sumfirstcol = numpy.sum(firstcol)
# Find the sum of the second column of data
sumsecondcol = numpy.sum(secondcol)
# Find the sum of the third column of data
sumthirdcol = numpy.sum(thirdcol)
# Find the sum of the fourth column of data
sumfourthcol = numpy.sum(fourthcol)

# Print the sum of the first column
print("Sum of first column is:", sumfirstcol)
# Print the sum of the second column
print("Sum of second column is:", sumsecondcol)
# Print the sum of the third column
print("Sum of third column is:", sumthirdcol)
# Print the sum if the fourth column
print("Sum of fourth column is:", sumfourthcol)