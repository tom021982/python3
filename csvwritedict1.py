
import csv

with open('Europe.csv', 'w', newline='') as csvfile:
    fieldnames = ['Country', 'Capital']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Country': 'France', 'Capital': 'Paris'})
    writer.writerow({'Country': 'Germany', 'Capital': 'Berlin'})
    writer.writerow({'Country': 'Russia', 'Capital': 'Moscow'})

