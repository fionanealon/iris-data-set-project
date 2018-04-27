# Fiona Nealon, 2018-04-27
# Iris data set analysis
# An alernative program to open a .csv file, read it, print it and close again

# Open .csv file with f as a variable
with open("data/iris.csv") as f:
# Loop through lines of file
  for line in f:
# Print lines of file
    print(line.split(',')[0])