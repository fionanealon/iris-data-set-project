# Fiona Nealon, 2018-04-28
# Iris data set analysis
# Create a scatter plot for petal and sepal width

# Use matplotlib & pyplot libraries to plot scatter plot
import matplotlib.pyplot as pl

# Use seaborn library to analyse data
import seaborn as sns

# Read csv file into python using seaborn
iris = sns.load_dataset("iris")

# Select all values in petal width array
iris["petal"] = iris["petal_width"]

# Select all values in sepal width array
iris["sepal"] = iris["sepal_width"]

# Adapted from: https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset 
# Use seaborn to compare variables
sns.lmplot(x="sepal", y="petal", data=iris, hue="species", fit_reg=False, legend=False)

# Add legend to scatter plot
pl.legend()

# Add title to scatter plot
pl.title('petal width and sepal width scatter plot')

# Output scatter plot
pl.show()