# Fiona Nealon, 2018-04-27
# Iris data set analysis
# A program to open a .csv file, read it, print it and close again

# Open iris.csv file in subfolder
f = open("data/iris.csv")

# Output information about file
print(f)

# Print contents of file
print(f.read())

# Close iris.csv file
f.close()