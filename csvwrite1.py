
import csv

with open('countries1.csv', 'w', newline='') as csvfile:
    listwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    listwriter.writerow(['Australia', 'NewZealand', 'Papua New Guinea'])
    listwriter.writerow(['Argentina', 'Chile', 'Peru', 'Brazil', 'Mexico'])
