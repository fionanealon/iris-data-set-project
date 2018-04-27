# Fiona Nealon, 2018-04-27
# Iris data set analysis
# An alernative program to open a .csv file, read it, print it and close again

# Open .csv file with f as a variable
with open("data/iris.csv") as f:
# Read contents of file
  contents = f.read()
# Print contents of file
  print(contents)
