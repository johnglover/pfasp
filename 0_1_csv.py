import csv

# open a file for writing
f = open("lac.csv", "wb")
writer = csv.writer(f)
# write data as comma-separated
# values
writer.writerows([
    ("2011", "Maynooth", 
     "Ireland"),
    ("2010", "Utrecht", 
     "The Netherlands"),
    ("2009", "Parma", 
     "Italy")])
f.close()

# read csv data
f = open("lac.csv", "rb")
venues = csv.reader(f)
# find and print the location
# of the 2011 LAC
for y, city, country, in venues:
    if y == "2011":
        print city, country
f.close()
