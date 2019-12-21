
import csv

with open('country.csv', newline='') as csvfile:
    listreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in listreader:
        print(','.join(row))
