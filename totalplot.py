# Fiona Nealon, 2018-04-28
# Iris data set analysis
# Plot histograms and scatterplots to analyse iris data set

# Use seaborn library to analyse data
import seaborn as sns

# Use matplotlib & pyplot libraries to plot histograms and scatter plot
import matplotlib.pyplot as plt

# Read csv file into python using numpy
iris = sns.load_dataset("iris")

# Adapted from: https://stackoverflow.com/questions/46383645/seaborn-and-pd-scatter-matrix-plot-color-issues
# Plot histograms ad scatter plots
sns.pairplot(iris, hue="species")

# Output the data
plt.show()
