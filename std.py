# Fiona Nealon, 2018-04-25
# Iris data set analysis

# Calculate the standard deviation of each column in the numpy array

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
# Find the maximum of the first column of data
maxfirstcol = numpy.std(firstcol)
# Find the maximum of the second column of data
maxsecondcol = numpy.std(secondcol)
# Find the maximum of the third column of data
maxthirdcol = numpy.std(thirdcol)
# Find the maximum of the fourth column of data
maxfourthcol = numpy.std(fourthcol)

# Print the standard deviatio of the first column 
print("Standard deviatioj of first column is:", maxfirstcol)
# Print the standard deviation of the second column 
print("Standard deviation of second column is:", maxsecondcol)
# Print the standard deviation of the third column 
print("Standard deviation of third column is:", maxthirdcol)
# Print the standard deviatioj of the fourth column 
print("Standrad deviation of fourth column is:", maxfourthcol)