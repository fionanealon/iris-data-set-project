import numpy

data = numpy.genfromtxt('data/iris.csv', delimiter=',')

fourthcol = data[:,3]

import matplotlib.pyplot as pl

pl.hist(fourthcol)

pl.title('petal_width histogram')

pl.show()