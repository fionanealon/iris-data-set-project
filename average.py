# Fiona Nealon, 2018-04-19
# Iris data set analysis

# Calculate the mean of each column.
import numpy

# Read data into array.
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]
meanfirstcol = numpy.mean(data[:,0])
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanfourthcol = numpy.mean(data[:,3])

print("Average of first column is:", meanfirstcol)
print("Average of second column is:", meansecondcol)
print("Average of third column is:", meanthirdcol)
print("Average of fourth column is:", meanfourthcol)
